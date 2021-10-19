# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the tsfpga project.
# https://tsfpga.com
# https://gitlab.com/tsfpga/tsfpga
# --------------------------------------------------------------------------------------------------

import copy
import hashlib
import datetime
import re
from shutil import copy2

from pathlib import Path

from tsfpga import DEFAULT_FILE_ENCODING
from tsfpga.git_utils import git_commands_are_available, get_git_commit
from tsfpga.svn_utils import svn_commands_are_available, get_svn_revision_information
from tsfpga.system_utils import create_directory, create_file, read_file
from . import __version__
from .constant import Constant
from .register import Register
from .register_array import RegisterArray
from .register_c_generator import RegisterCGenerator
from .register_cpp_generator import RegisterCppGenerator
from .register_html_generator import RegisterHtmlGenerator
from .register_python_generator import RegisterPythonGenerator
from .register_vhdl_generator import RegisterVhdlGenerator


class RegisterList:

    """
    Used to handle the registers of a module. Also known as a register map.
    """

    def __init__(self, name, source_definition_file):
        """
        Arguments:
            name (str): The name of this register list. Typically the name of the module that uses
                it.
            source_definition_file (`pathlib.Path`): The TOML source file that defined this
                register list. Will be displayed in generated source code and documentation
                for traceability.
        """
        self.name = name
        self.source_definition_file = source_definition_file

        self.register_objects = []
        self.constants = []

    @classmethod
    def from_default_registers(cls, name, source_definition_file, default_registers):
        """
        Factory method. Create a RegisterList object from a plain list of registers.

        Arguments:
            name (str): The name of this register list.
            source_definition_file (`pathlib.Path`): The source file that defined this
                register list. Will be displayed in generated source code and documentation
                for traceability.

                Can be set to ``None`` if this information does not make sense in the current
                use case.
            default_registers (list(.Register)): These registers will be inserted in the
               register list.
        """
        register_list = cls(name=name, source_definition_file=source_definition_file)
        register_list.register_objects = copy.deepcopy(default_registers)
        return register_list

    def append_register(self, name, mode, description):
        """
        Append a register to this list.

        Arguments:
            name (str): The name of the register.
            mode (str): A valid register mode.
            description (str): Textual register description.
        Return:
            :class:`.Register`: The register object that was created.
        """
        if self.register_objects:
            index = self.register_objects[-1].index + 1
        else:
            index = 0

        register = Register(name, index, mode, description)
        self.register_objects.append(register)

        return register

    def append_register_array(self, name, length, description):
        """
        Append a register array to this list.

        Arguments:
            name (str): The name of the register array.
            length (int): The number of times the register sequence shall be repeated.
        Return:
            :class:`.RegisterArray`: The register array object that was created.
        """
        if self.register_objects:
            base_index = self.register_objects[-1].index + 1
        else:
            base_index = 0
        register_array = RegisterArray(
            name=name, base_index=base_index, length=length, description=description
        )

        self.register_objects.append(register_array)
        return register_array

    def get_register(self, name):
        """
        Get a register from this list. Will only find single registers, not registers in a
        register array. Will raise exception if no register matches.

        Arguments:
            name (str): The name of the register.
        Return:
            :class:`.Register`: The register.
        """
        for register_object in self.register_objects:
            if isinstance(register_object, Register) and register_object.name == name:
                return register_object

        raise ValueError(f'Could not find register "{name}" within register list "{self.name}"')

    def get_register_array(self, name):
        """
        Get a register array from this list. Will raise exception if no register array matches.

        Arguments:
            name (str): The name of the register array.
        Return:
            :class:`.RegisterArray`: The register array.
        """
        for register_object in self.register_objects:
            if isinstance(register_object, RegisterArray) and register_object.name == name:
                return register_object

        raise ValueError(
            f'Could not find register array "{name}" within register list "{self.name}"'
        )

    def get_register_index(
        self, register_name, register_array_name=None, register_array_index=None
    ):
        """
        Get the zero-based index within the register list for the specified register.

        Arguments:
            register_name (str): The name of the register.
            register_array_name (str): If the register is within a register array the name
                of the array must be specified.
            register_array_name (str): If the register is within a register array the array
                iteration index must be specified.

        Return:
            int: The index.
        """
        if register_array_name is None and register_array_index is None:
            # Target is plain register
            register = self.get_register(register_name)

            return register.index

        # Target is in register array
        register_array = self.get_register_array(register_array_name)
        register_array_start_index = register_array.get_start_index(register_array_index)

        register = register_array.get_register(register_name)
        register_index = register.index

        return register_array_start_index + register_index

    def add_constant(self, name, value, description=None):
        """
        Add a constant. Will be available in the generated packages and headers.

        Arguments:
            name (str): The name of the constant.
            length (int): The constant value (signed).
            description (str): Textual description for the constant.
        Return:
            :class:`.Constant`: The constant object that was created.
        """
        constant = Constant(name, value, description)
        self.constants.append(constant)
        return constant

    def get_constant(self, name):
        """
        Get a constant from this list. Will raise exception if no constant matches.

        Arguments:
            name (str): The name of the constant.
        Return:
            :class:`.Constant`: The constant.
        """
        for constant in self.constants:
            if constant.name == name:
                return constant

        raise ValueError(f'Could not find constant "{name}" within register list "{self.name}"')

    def create_vhdl_package(self, output_path):
        """
        Create a VHDL package file with register and field definitions.

        This function assumes that the ``output_path`` folder already exists. This assumption makes
        it slightly faster than the other functions that use ``create_file()``. Necessary since this
        one is often used in real time (before simulations, etc..) and not in one-off scenarios
        like the others (when making a release).

        In order to save time, there is a mechanism to only generate the VHDL file when necessary.
        A hash of this register list object will be written to the file along with all the register
        definitions. This hash will be inspected and compared, and the VHDL file will only be
        generated again if something has changed.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        vhd_file = output_path / (self.name + "_regs_pkg.vhd")

        self_hash = self._hash()
        if self._should_create_vhdl_package(vhd_file, self_hash):
            self._create_vhdl_package(vhd_file, self_hash)

    def _should_create_vhdl_package(self, vhd_file, self_hash):
        if not vhd_file.exists():
            return True
        if (self_hash, __version__) != self._find_hash_and_version_of_existing_vhdl_package(
            vhd_file
        ):
            return True
        return False

    @staticmethod
    def _find_hash_and_version_of_existing_vhdl_package(vhd_file):
        """
        Returns `None` if nothing found, otherwise the matching strings in a tuple.
        """
        regexp = re.compile(
            r"\n-- Register hash ([0-9a-f]+), generator version (\d+\.\d+\.\d+)\.\n"
        )
        existing_file_content = read_file(vhd_file)
        match = regexp.search(existing_file_content)
        if match is None:
            return None
        return match.group(1), match.group(2)

    def _create_vhdl_package(self, vhd_file, self_hash):
        print(f"Creating VHDL register package {vhd_file}")
        # Add a header line with the hash
        generated_info = self.generated_source_info() + [
            f"Register hash {self_hash}, generator version {__version__}."
        ]
        register_vhdl_generator = RegisterVhdlGenerator(self.name, generated_info)
        with open(vhd_file, "w", encoding=DEFAULT_FILE_ENCODING) as file_handle:
            file_handle.write(
                register_vhdl_generator.get_package(self.register_objects, self.constants)
            )

    def create_c_header(self, output_path):
        """
        Create a C header file with register and field definitions.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        output_file = output_path / (self.name + "_regs.h")
        register_c_generator = RegisterCGenerator(self.name, self.generated_source_info())
        create_file(
            output_file, register_c_generator.get_header(self.register_objects, self.constants)
        )

    def create_cpp_interface(self, output_path):
        """
        Create a C++ class interface header file, with register and field definitions. The
        interface header contains only virtual methods.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        output_file = output_path / ("i_" + self.name + ".h")
        register_cpp_generator = RegisterCppGenerator(self.name, self.generated_source_info())
        create_file(
            output_file, register_cpp_generator.get_interface(self.register_objects, self.constants)
        )

    def create_cpp_header(self, output_path):
        """
        Create a C++ class header file.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        output_file = output_path / (self.name + ".h")
        register_cpp_generator = RegisterCppGenerator(self.name, self.generated_source_info())
        create_file(output_file, register_cpp_generator.get_header(self.register_objects))

    def create_cpp_implementation(self, output_path):
        """
        Create a C++ class implementation file.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        output_file = output_path / (self.name + ".cpp")
        register_cpp_generator = RegisterCppGenerator(self.name, self.generated_source_info())
        create_file(output_file, register_cpp_generator.get_implementation(self.register_objects))

    def create_html_page(self, output_path):
        """
        Create a documentation HTML page with register and field information. Will include the
        tables created by :meth:`.create_html_register_table` and
        :meth:`.create_html_constant_table`.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        register_html_generator = RegisterHtmlGenerator(self.name, self.generated_source_info())

        html_file = output_path / (self.name + "_regs.html")
        create_file(
            html_file, register_html_generator.get_page(self.register_objects, self.constants)
        )

        stylesheet = register_html_generator.get_page_style()
        stylesheet_file = output_path / "regs_style.css"
        if (not stylesheet_file.exists()) or read_file(stylesheet_file) != stylesheet:
            # Create the file only once. This mechanism could be made more smart, but at the moment
            # there is no use case. Perhaps there should be a separate stylesheet for each
            # HTML file?
            create_file(stylesheet_file, stylesheet)

    def create_html_register_table(self, output_path):
        """
        Create documentation HTML table with register and field information.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        output_file = output_path / (self.name + "_register_table.html")
        register_html_generator = RegisterHtmlGenerator(self.name, self.generated_source_info())
        create_file(output_file, register_html_generator.get_register_table(self.register_objects))

    def create_html_constant_table(self, output_path):
        """
        Create documentation HTML table with constant information.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        output_file = output_path / (self.name + "_constant_table.html")
        register_html_generator = RegisterHtmlGenerator(self.name, self.generated_source_info())
        create_file(output_file, register_html_generator.get_constant_table(self.constants))

    def create_python_class(self, output_path):
        """
        Save a python class with all register and constant information.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        register_python_generator = RegisterPythonGenerator(self.name, self.generated_source_info())
        register_python_generator.create_class(register_list=self, output_folder=output_path)

    def copy_source_definition(self, output_path):
        """
        Copy the source file that created this register list. If no source file is set, nothing will
        be copied.

        Arguments:
            output_path (`pathlib.Path`): Result will be placed here.
        """
        if self.source_definition_file is not None:
            create_directory(output_path, empty=False)
            copy2(self.source_definition_file, output_path)

    @staticmethod
    def generated_info():
        """
        Return:
            list(str): Line(s) informing the user that a file is automatically generated.
        """
        return ["This file is automatically generated by tsfpga."]

    def generated_source_info(self):
        """
        Return:
            list(str): Line(s) informing the user that a file is automatically generated, containing
            info about the source of the generated register information.
        """
        # Default to the user's current working directory
        directory = Path(".")

        time_info = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        file_info = ""
        if self.source_definition_file is not None:
            directory = self.source_definition_file.parent
            file_info = f" from file {self.source_definition_file.name}"

        commit_info = ""
        if git_commands_are_available(directory):
            commit_info = f" at commit {get_git_commit(directory)}"
        elif svn_commands_are_available(directory):
            commit_info = f" at revision {get_svn_revision_information(directory)}"

        info = f"Generated {time_info}{file_info}{commit_info}."

        return self.generated_info() + [info]

    def _hash(self):
        """
        Get a hash of this object representation. SHA1 is the fastest method according to e.g.
        http://atodorov.org/blog/2013/02/05/performance-test-md5-sha1-sha256-sha512/
        Result is a lowercase hexadecimal string.
        """
        return hashlib.sha1(repr(self).encode()).hexdigest()

    def __repr__(self):
        return f"""{self.__class__.__name__}(\
name={self.name},\
source_definition_file={repr(self.source_definition_file)},\
register_objects={','.join([repr(register_object) for register_object in self.register_objects])},\
constants={','.join([repr(constant) for constant in self.constants])},\
)"""
