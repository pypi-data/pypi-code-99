import sys
from argparse import ArgumentParser, SUPPRESS
from unittest import skipIf, TestCase
from unittest.mock import Mock, patch

from corgy import CorgyHelpFormatter
from corgy._helpfmt import _ColorHelper

if sys.version_info >= (3, 9):
    from argparse import BooleanOptionalAction

_COLOR_HELPER = _ColorHelper(skip_tty_check=True)
_CRAYONS = _COLOR_HELPER.crayons

# Shortcuts for color functions to make ground truths in assert statements concise.
_M = lambda s: _COLOR_HELPER.colorize(s, CorgyHelpFormatter.color_metavars)
_K = lambda s: _COLOR_HELPER.colorize(s, CorgyHelpFormatter.color_keywords)
_C = lambda s: _COLOR_HELPER.colorize(repr(s), CorgyHelpFormatter.color_choices)
_D = lambda s: _COLOR_HELPER.colorize(repr(s), CorgyHelpFormatter.color_defaults)
_O = lambda s: _COLOR_HELPER.colorize(s, CorgyHelpFormatter.color_options)

# Version of `_C` which does not call `repr` on the object.
_Cs = lambda s: _COLOR_HELPER.colorize(s, CorgyHelpFormatter.color_choices)

# Make outputs independent of terminal width.
CorgyHelpFormatter.output_width = 80
CorgyHelpFormatter.max_help_position = 80

# The default choice list end markers, `{`, `}`, make f-strings messy, since they need
# to be escaped. So, we  replace them with `[`, `]`.
CorgyHelpFormatter.marker_choices_begin = "["
CorgyHelpFormatter.marker_choices_end = "]"


class TestCorgyHelpFormatterAPI(TestCase):
    """Tests to check behavior of the `CorgyHelpFormatter` API."""

    def test_corgy_help_formatter_raises_if_enabling_colors_without_crayons(self):
        CorgyHelpFormatter.use_colors = True
        with patch(
            "corgy._helpfmt.importlib.import_module", Mock(side_effect=ImportError)
        ):
            with self.assertRaises(ImportError):
                ArgumentParser(formatter_class=CorgyHelpFormatter)

    def test_corgy_help_formatter_doesnt_raise_if_use_colors_none_without_crayons(self):
        CorgyHelpFormatter.use_colors = None
        with patch(
            "corgy._helpfmt.importlib.import_module", Mock(side_effect=ImportError)
        ):
            try:
                ArgumentParser(formatter_class=CorgyHelpFormatter)
            except ImportError:
                self.fail()

    def test_corgy_help_formatter_raises_if_setting_new_attribute(self):
        with self.assertRaises(AttributeError):
            CorgyHelpFormatter.foo = "bar"

    @skipIf(_CRAYONS is None, "`crayons` package not found")
    def test_corgy_help_formatter_handles_changing_colors(self):
        CorgyHelpFormatter.use_colors = True
        with patch.multiple(
            CorgyHelpFormatter,
            color_choices="red",
            color_defaults="BLUE",
            color_keywords="BOLD",
            color_metavars="BLUE",
            color_options="yellow",
        ):
            parser = ArgumentParser(formatter_class=CorgyHelpFormatter, add_help=False)
            parser.add_argument(
                "--x", type=int, choices=[1, 2], help="x help", default=1
            )

            self.assertEqual(
                parser.format_help(),
                # options:
                #   --x int  x help ([1/2] default: 1)
                f"options:\n"
                f"  {_COLOR_HELPER.colorize('--x', 'yellow')} "
                f"{_COLOR_HELPER.colorize('int', 'BLUE')}  "
                f"x help ([{_COLOR_HELPER.colorize(1, 'red')}/"
                f"{_COLOR_HELPER.colorize(2, 'red')}] "
                f"{_COLOR_HELPER.colorize('default', 'BOLD')}: "
                f"{_COLOR_HELPER.colorize(1, 'BLUE')})\n",
            )

    def test_corgy_help_formatter_handles_changing_markers(self):
        CorgyHelpFormatter.use_colors = False
        with patch.multiple(
            CorgyHelpFormatter,
            marker_extras_begin="%",
            marker_extras_end="%",
            marker_choices_begin=" ( ",
            marker_choices_end=" ) ",
            marker_choices_sep="|",
        ):
            parser = ArgumentParser(formatter_class=CorgyHelpFormatter, add_help=False)
            parser.add_argument("-x", "--x", type=int, choices=[1, 2])

            self.assertEqual(
                parser.format_help(), "options:\n  -x|--x int  % ( 1|2 )  optional%\n"
            )

    def test_corgy_help_formatter_handles_changing_output_width(self):
        CorgyHelpFormatter.use_colors = False
        with patch.object(CorgyHelpFormatter, "output_width", 10):
            parser = ArgumentParser(formatter_class=CorgyHelpFormatter, add_help=False)
            parser.add_argument("--x", type=int, help="x help")

            self.assertEqual(
                parser.format_help(),
                "options:\n"
                "  --x int\n"
                "      x\n"
                "      help\n"
                "      (opt\n"
                "      iona\n"
                "      l)\n",
            )

    def test_corgy_help_formatter_handles_changing_max_help_position(self):
        CorgyHelpFormatter.use_colors = False
        with patch.multiple(CorgyHelpFormatter, output_width=100, max_help_position=10):
            parser = ArgumentParser(formatter_class=CorgyHelpFormatter)
            parser.add_argument(
                "--x", type=int, metavar="A LONG METAVAR", help="x help"
            )

            self.assertEqual(
                parser.format_help(),
                # options:
                #   -h/--help
                #       show this help message and exit (optional)
                #   --x A LONG METAVAR
                #       x help (optional)
                "options:\n"
                "  -h/--help\n"
                "      show this help message and exit (optional)\n"
                "  --x A LONG METAVAR\n"
                "      x help (optional)\n",
            )

    @skipIf(_CRAYONS is None, "`crayons` package not found")
    def test_corgy_help_formatter_consistent_on_repeat_usage(self):
        CorgyHelpFormatter.use_colors = True
        parser = ArgumentParser(formatter_class=CorgyHelpFormatter)
        parser.add_argument("--x", type=int, choices=[1, 2])

        desired_output = (
            # options:
            #   -h/--help  show this help message and exit (optional)
            #   --x int    ([1/2] optional)
            f"options:\n"
            f"  {_O('-h')}/{_O('--help')}  show this help message and exit "
            f"({_K('optional')})\n"
            f"  {_O('--x')} {_M('int')}    ([{_C(1)}/{_C(2)}] {_K('optional')})\n"
        )

        self.assertEqual(parser.format_help(), desired_output)
        self.assertEqual(parser.format_help(), desired_output)

        # Test with a new parser.
        parser = ArgumentParser(formatter_class=CorgyHelpFormatter)
        parser.add_argument("--x", type=int, choices=[1, 2])
        self.assertEqual(parser.format_help(), desired_output)

    def test_corgy_help_formatter_does_not_construct_usage_if_none_provided(self):
        parser = ArgumentParser(formatter_class=CorgyHelpFormatter)
        self.assertEqual(parser.format_usage(), "")

    def test_corgy_help_formatter_shows_custom_usage_iff_called_directly(self):
        parser = ArgumentParser(
            formatter_class=CorgyHelpFormatter, add_help=False, usage="custom usage"
        )
        self.assertEqual(parser.format_usage(), "usage: custom usage\n")
        self.assertEqual(parser.format_help(), "")

    @skipIf(_CRAYONS is None, "`crayons` package not found")
    def test_corgy_help_formatter_raises_if_using_invalid_color(self):
        with patch.object(CorgyHelpFormatter, "color_metavars", "ELUB"):
            parser = ArgumentParser(formatter_class=CorgyHelpFormatter)
            parser.add_argument("--x", type=str)
            with self.assertRaises(ValueError):
                parser.format_help()


@skipIf(_CRAYONS is None, "`crayons` package not found")
class TestCorgyHelpFormatterSingleArgs(TestCase):
    """Tests to check formatting of single arguments."""

    def setUp(self):
        _COLOR_HELPER.crayons = _CRAYONS
        CorgyHelpFormatter.use_colors = True
        self.parser = ArgumentParser(formatter_class=CorgyHelpFormatter, add_help=False)
        self.maxDiff = None  # color codes can lead to very long diffs

    def _get_arg_help(self, *args, **kwargs):
        """Add a parser argument using `args` and `kwargs`, and return the help output.

        Only the output for the particular argument is returned.
        """
        self.parser.add_argument(*args, **kwargs)
        _help = self.parser.format_help()
        if _help:
            return _help.split("\n", maxsplit=1)[1].rstrip()
        return ""

    def test_corgy_help_formatter_handles_positional_arg_without_help(self):
        self.assertEqual(
            self._get_arg_help("arg", type=str),
            #   arg str
            f"  {_O('arg')} {_M('str')}",
        )

    def test_corgy_help_formatter_handles_required(self):
        self.assertEqual(
            self._get_arg_help("--x", type=str, required=True),
            #   --x str  (required)
            f"  {_O('--x')} {_M('str')}  ({_K('required')})",
        )

    def test_corgy_help_formatter_handles_optional(self):
        self.assertEqual(
            self._get_arg_help("--x", type=str),
            #   --x str  (optional)
            f"  {_O('--x')} {_M('str')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_default(self):
        self.assertEqual(
            self._get_arg_help("--x", type=str, default="def"),
            #   --x str  (default: def)
            f"  {_O('--x')} {_M('str')}  ({_K('default')}: {_D('def')})",
        )

    def test_corgy_help_formatter_handles_choices(self):
        self.assertEqual(
            self._get_arg_help("--x", type=str, choices=["a", "b"]),
            #   --x str  ([a/b] optional)
            f"  {_O('--x')} {_M('str')}  ([{_C('a')}/{_C('b')}] {_K('optional')})",
        )

    def test_corgy_help_formatter_handles_choices_with_default(self):
        self.assertEqual(
            self._get_arg_help("--x", type=str, default="def", choices=["a", "b"]),
            #  --x str  ([a/b] default: def)
            f"  {_O('--x')} {_M('str')}  ([{_C('a')}/{_C('b')}] "
            f"{_K('default')}: {_D('def')})",
        )

    def test_corgy_help_formatter_handles_help_text(self):
        self.assertEqual(
            self._get_arg_help("--x", help="x help", type=str),
            #   --x str  x help (optional)
            f"  {_O('--x')} {_M('str')}  x help ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_option_aliases(self):
        self.assertEqual(
            self._get_arg_help("-x", "--ex", "--between-y-and-z", type=str),
            # -x/--ex/--between-y-and-z str  (optional)
            f"  {_O('-x')}/{_O('--ex')}/{_O('--between-y-and-z')} {_M('str')}  "
            f"({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_long_option(self):
        with patch.object(CorgyHelpFormatter, "output_width", 10):
            self.assertEqual(
                self._get_arg_help("--avery-long-argument-name", type=str),
                #   --avery-
                #     long-a
                #     rgumen
                #     t-name
                #     str
                #       (opt
                #       iona
                #       l)
                f"  {_O('--avery-')}\n"
                f"    {_O('long-a')}\n"
                f"    {_O('rgumen')}\n"
                f"    {_O('t-name')}\n"
                f"    {_M('str')}\n"
                f"      ({_K('opt')}\n"
                f"      {_K('iona')}\n"
                f"      {_K('l')})",
            )

    def test_corgy_help_formatter_handles_different_prefix_chars(self):
        with patch.object(self.parser, "prefix_chars", "+++"):
            self.assertEqual(
                self._get_arg_help("+++x", type=str, help="x help"),
                #   +++x str  x help (optional)
                f"  {_O('+++x')} {_M('str')}  x help ({_K('optional')})",
            )

    @skipIf(sys.version_info < (3, 9), "`BooleanOptionalAction` not available")
    def test_corgy_help_formatter_handles_boolean_optional_action(self):
        self.assertEqual(
            self._get_arg_help(
                "--x", action=BooleanOptionalAction, help="x help", default=True
            ),
            #   --x/--no-x  x help (default: True)
            f"  {_O('--x')}/{_O('--no-x')}  x help ({_K('default')}: {_D(True)})",
        )

    def test_corgy_help_formatter_handles_help_suppress(self):
        self.assertEqual(
            self._get_arg_help("--x", type=str, help=SUPPRESS, default="def"), ""
        )

    def test_corgy_help_formatter_handles_nargs_plus(self):
        self.assertEqual(
            self._get_arg_help("--x", nargs="+", type=str),
            #   --x str [str ...]  (optional)
            f"  {_O('--x')} {_M('str')} [{_M('str')} ...]  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_nargs_const(self):
        self.assertEqual(
            self._get_arg_help("--x", nargs=3, type=str),
            #   --x str str str  (optional)
            f"  {_O('--x')} {_M('str')} {_M('str')} {_M('str')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_nargs_suppress(self):
        self.assertEqual(
            self._get_arg_help("--x", nargs=SUPPRESS, type=str),
            #   --x  (optional)
            f"  {_O('--x')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_tuple_metavar(self):
        self.assertEqual(
            self._get_arg_help("--x", metavar=("M1", "M2"), nargs=2),
            #   --x M1 M2  (optional)
            f"  {_O('--x')} {_M('M1')} {_M('M2')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_tuple_metavar_with_nargs_plus(self):
        self.assertEqual(
            self._get_arg_help("--x", metavar=("M1", "M2"), nargs="+"),
            #   --x M1 [M2 ...]  (optional)
            f"  {_O('--x')} {_M('M1')} [{_M('M2')} ...]  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_custom_type(self):
        class CustomType:
            pass

        self.assertEqual(
            self._get_arg_help("--x", type=CustomType),
            #   --x CustomType  (optional)
            f"  {_O('--x')} {_M('CustomType')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_callable_type(self):
        def custom_type(s):
            return s

        self.assertEqual(
            self._get_arg_help("--x", type=custom_type),
            #   --x custom_type  (optional)
            f"  {_O('--x')} {_M('custom_type')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_custom_metavar(self):
        class CustomType:
            __metavar__ = "CUSTOM"

        self.assertEqual(
            self._get_arg_help("--x", type=CustomType),
            #   --x CUSTOM  (optional)
            f"  {_O('--x')} {_M('CUSTOM')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_missing_type(self):
        self.assertEqual(
            self._get_arg_help("--x", type=None),
            #   --x  (optional)
            f"  {_O('--x')}  ({_K('optional')})",
        )

    def test_corgy_help_formatter_handles_long_metavar(self):
        class CustomType:
            __metavar__ = "A-VERY-VERY-LONG-METAVAR"

        with patch.object(CorgyHelpFormatter, "output_width", 10):
            self.assertEqual(
                self._get_arg_help("--x", type=CustomType),
                #   --x A-VE
                #     RY-VER
                #     Y-LONG
                #     -METAV
                #     AR
                #       (opt
                #       iona
                #       l)
                f"  {_O('--x')} {_M('A-VE')}\n"
                f"    {_M('RY-VER')}\n"
                f"    {_M('Y-LONG')}\n"
                f"    {_M('-METAV')}\n"
                f"    {_M('AR')}\n"
                f"      ({_K('opt')}\n"
                f"      {_K('iona')}\n"
                f"      {_K('l')})",
            )

    def test_corgy_help_formatter_handles_long_help(self):
        with patch.object(CorgyHelpFormatter, "output_width", 15):
            self.assertEqual(
                self._get_arg_help("--x", type=str, help="a very lengthy help"),
                #   --x str  a
                #            very
                #            leng
                #            thy
                #            help
                #            (opt
                #            iona
                #            l)
                f"  {_O('--x')} {_M('str')}  a\n"
                f"           very\n"
                f"           leng\n"
                f"           thy\n"
                f"           help\n"
                f"           ({_K('opt')}\n"
                f"           {_K('iona')}\n"
                f"           {_K('l')})",
            )

    def test_corgy_help_formatter_handles_long_help_with_small_max_help_pos(self):
        with patch.multiple(CorgyHelpFormatter, output_width=15, max_help_position=5):
            self.assertEqual(
                self._get_arg_help("--x", type=str, help="a very lengthy help"),
                #   --x str
                #       a very
                #       lengthy
                #       help (opt
                #       ional)
                f"  {_O('--x')} {_M('str')}\n"
                f"      a very\n"
                f"      lengthy\n"
                f"      help ({_K('opt')}\n"
                f"      {_K('ional')})",
            )

    def test_corgy_help_formatter_handles_conflicting_text_in_help(self):
        self.assertEqual(
            self._get_arg_help(
                "--x",
                type=int,
                choices=[1, 2],
                default=1,
                help="--x int  x help ([1/2] default: 1)",
            ),
            #   --x int  x help ([1/2] default: 1) ([1/2] default: 1)
            f"  {_O('--x')} {_M('int')}  --x int  x help ([1/2] default: 1) "
            f"([{_C(1)}/{_C(2)}] {_K('default')}: {_D(1)})",
        )

    def test_corgy_help_formatter_handles_conflicting_text_in_choice(self):

        with patch.object(CorgyHelpFormatter, "output_width", 200):
            self.assertEqual(
                self._get_arg_help(
                    "--x",
                    type=str,
                    choices=[
                        "a",
                        "b",
                        "--x str",
                        "['a'/\"b\"]",
                        "default: 'a'",
                        "--x str  x help (['a'/\"b\"] default: 'a')",
                    ],
                    default="a",
                    help="x help",
                ),
                # This is awful.
                #   --x str  x help ([
                f"  {_O('--x')} {_M('str')}  x help (["
                # 'a'/'b'/
                + _C("a") + "/" + _C("b") + "/"
                # '--x str/'
                + _Cs("'--x") + " " + _Cs("str'") + "/"
                # '[\'a\'/"b"]'/
                + _Cs("'[\\'a\\'/\"b\"]'") + "/"
                # "default: 'a'"/
                + _Cs('"default:') + " " + _Cs("'a'\"") + "/"
                # '--x str  x help
                + _Cs("'--x") + " " + _Cs("str") + "  " + _Cs("x") + " " + _Cs("help")
                #  ([\'a\'/"b"]
                + " " + _Cs("([\\'a\\'/\"b\"]")
                #  default: \'a\')}
                + " " + _Cs("default:") + " " + _Cs("\\'a\\')'") + "] "
                # default: 'a'
                + f"{_K('default')}: {_D('a')})",
            )

    def test_corgy_help_formatter_handles_long_choice(self):
        _q = "'"  # can't use escapes inside f-strings
        with patch.multiple(CorgyHelpFormatter, output_width=15, max_help_position=5):
            self.assertEqual(
                self._get_arg_help(
                    "--x",
                    type=str,
                    choices=["a", "supercalifragilisticexpialidocious choice", "b"],
                    default="a",
                ),
                #   --x str
                #       (['a'/'su
                #       percalifr
                #       agilistic
                #       expialido
                #       cious cho
                #       ice'/'b']
                #       default:
                #       'a')
                f"  {_O('--x')} {_M('str')}\n"
                f"      ([{_C('a')}/{_Cs(_q+'su')}\n"
                f"      {_Cs('percalifr')}\n"
                f"      {_Cs('agilistic')}\n"
                f"      {_Cs('expialido')}\n"
                f"      {_Cs('cious')} {_Cs('cho')}\n"
                f"      {_Cs('ice'+_q)}/{_C('b')}]\n"
                f"      {_K('default')}:\n"
                f"      {_D('a')})",
            )

    def test_corgy_help_formatter_handles_default_suppress(self):
        self.assertEqual(
            self._get_arg_help("--arg", type=str, default=SUPPRESS),
            f"  {_O('--arg')} {_M('str')}  ({_K('optional')})",
        )


@skipIf(_CRAYONS is None, "`crayons` package not found")
class TestCorgyHelpFormatterMultiArgs(TestCase):
    """Tests to check formatting of multiple arguments together."""

    def setUp(self):
        _COLOR_HELPER.crayons = _CRAYONS
        CorgyHelpFormatter.use_colors = True
        self.parser = ArgumentParser(formatter_class=CorgyHelpFormatter)
        self.maxDiff = None

    def test_corgy_help_formatter_handles_multi_arg_alignment(self):
        self.parser.add_argument("--x", type=int, help="x help")
        self.parser.add_argument("-y", "--why", type=float, required=True)
        self.parser.add_argument("-z", type=str, default="z", help="z help")

        self.assertEqual(
            self.parser.format_help(),
            # options:
            #   -h/--help       show this help message and exit (optional)
            #   --x int         x help
            #   -y/--why float  (required)
            #   -z str          z help (default: 'z')
            f"options:\n"
            f"  {_O('-h')}/{_O('--help')}       show this help message and exit "
            f"({_K('optional')})\n"
            f"  {_O('--x')} {_M('int')}         x help ({_K('optional')})\n"
            f"  {_O('-y')}/{_O('--why')} {_M('float')}  ({_K('required')})\n"
            f"  {_O('-z')} {_M('str')}          z help ({_K('default')}: {_D('z')})\n",
        )

    def test_corgy_help_formatter_handles_multi_arg_wrapping(self):
        self.parser.add_argument("-x", "--ex", type=float, help="help" * 10)
        with patch.object(CorgyHelpFormatter, "output_width", 30):
            self.assertEqual(
                self.parser.format_help(),
                # options:
                #   -h/--help      show this
                #                  help message
                #                  and exit
                #                  (optional)
                #   -x/--ex float  helphelphelph
                #                  elphelphelphe
                #                  lphelphelphel
                #                  p (optional)
                f"options:\n"
                f"  {_O('-h')}/{_O('--help')}      show this\n"
                f"                 help message\n"
                f"                 and exit\n"
                f"                 ({_K('optional')})\n"
                f"  {_O('-x')}/{_O('--ex')} {_M('float')}  helphelphelph\n"
                f"                 elphelphelphe\n"
                f"                 lphelphelphel\n"
                f"                 p ({_K('optional')})\n",
            )

    def test_corgy_help_formatter_handles_multi_arg_with_small_max_help_pos(self):
        self.parser.add_argument("-x", "--ex", type=float, help="help" * 10)
        with patch.object(CorgyHelpFormatter, "max_help_position", 10):
            self.assertEqual(
                self.parser.format_help(),
                # options:
                #   -h/--help
                #       show this help message and exit (optional)
                #   -x/--ex float
                #       helphelphelphelphelphelphelphelphelphelp (optional)
                f"options:\n"
                f"  {_O('-h')}/{_O('--help')}\n"
                f"      show this help message and exit ({_K('optional')})\n"
                f"  {_O('-x')}/{_O('--ex')} {_M('float')}\n"
                f"      helphelphelphelphelphelphelphelphelphelp ({_K('optional')})\n",
            )

    def test_corgy_help_formatter_handles_argument_groups(self):
        self.parser.add_argument("arg", help="arg help")
        self.parser.add_argument("--x", type=str, help="x help")
        grp_parser = self.parser.add_argument_group("group 1")
        grp_parser.add_argument("--y", required=True)
        grp_parser.add_argument("--z", type=float)
        grp_parser = self.parser.add_argument_group("group 2", "group 2 description")
        grp_parser.add_argument("--w", type=str)

        self.assertEqual(
            self.parser.format_help(),
            # positional arguments:
            #   arg        arg help
            #
            # options:
            #   -h/--help  show this help message and exit (optional)
            #   --x str    x help (optional)
            #
            # group 1:
            #   --y        (required)
            #   --z float  (optional)
            #
            # group 2:
            #   group 2 description
            #   --w str    (optional)
            f"positional arguments:\n"
            f"  {_O('arg')}        arg help\n"
            f"\n"
            f"options:\n"
            f"  {_O('-h')}/{_O('--help')}  show this help message and exit "
            f"({_K('optional')})\n"
            f"  {_O('--x')} {_M('str')}    x help ({_K('optional')})\n"
            f"\n"
            f"group 1:\n"
            f"  {_O('--y')}        ({_K('required')})\n"
            f"  {_O('--z')} {_M('float')}  ({_K('optional')})\n"
            f"\n"
            f"group 2:\n"
            f"  group 2 description\n"
            f"\n"
            f"  {_O('--w')} {_M('str')}    ({_K('optional')})\n",
        )

    def test_corgy_help_formatter_handles_sub_parsers(self):
        self.parser.add_argument("--arg", type=str)
        subparsers = self.parser.add_subparsers(help="sub commands")
        subparsers.add_parser("x", formatter_class=CorgyHelpFormatter)
        subparsers.add_parser("y", formatter_class=CorgyHelpFormatter)

        self.assertEqual(
            self.parser.format_help(),
            # positional arguments:
            #   CMD        sub commands (['x'/'y'])
            #
            # options:
            #   -h/--help  show this help message and exit (optional)
            #   --arg str  (optional)
            f"positional arguments:\n"
            f"  {_O('CMD')}        sub commands ([{_C('x')}/{_C('y')}])\n"
            f"\n"
            f"options:\n"
            f"  {_O('-h')}/{_O('--help')}  show this help message and exit "
            f"({_K('optional')})\n"
            f"  {_O('--arg')} {_M('str')}  ({_K('optional')})\n",
        )


class _NoColorTestMeta(type):
    """Metaclass to create versions of test classes that don't use colors."""

    def __new__(cls, name, bases, namespace, **kwds):
        for _item in dir(bases[0]):
            if not _item.startswith("test_"):
                continue
            test_fn = getattr(bases[0], _item)
            new_test_fn_name = f"{_item}_no_color"
            namespace[new_test_fn_name] = test_fn

        bases = (TestCase,)  # to prevent duplication of tests in the base class
        return super().__new__(cls, name, bases, namespace, **kwds)


class TestCorgyHelpFormatterSingleArgsNoColor(
    TestCorgyHelpFormatterSingleArgs, metaclass=_NoColorTestMeta
):
    """Tests to check formatting of single arguments without colors."""

    # The metaclass removes the base class from the inheritance chain, so we need to
    # manually inherit needed base class methods.
    _get_arg_help = TestCorgyHelpFormatterSingleArgs._get_arg_help

    def setUp(self):
        _COLOR_HELPER.crayons = None
        CorgyHelpFormatter.use_colors = False
        self.parser = ArgumentParser(formatter_class=CorgyHelpFormatter, add_help=False)


class TestCorgyHelpFormatterMultiArgsNoColor(
    TestCorgyHelpFormatterMultiArgs, metaclass=_NoColorTestMeta
):
    """Tests to check formatting of multiple arguments together without colors."""

    def setUp(self):
        _COLOR_HELPER.crayons = None
        CorgyHelpFormatter.use_colors = False
        self.parser = ArgumentParser(formatter_class=CorgyHelpFormatter)
