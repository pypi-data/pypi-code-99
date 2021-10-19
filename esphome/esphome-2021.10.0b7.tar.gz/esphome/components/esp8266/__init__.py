import logging

from esphome.const import (
    CONF_BOARD,
    CONF_BOARD_FLASH_MODE,
    CONF_FRAMEWORK,
    CONF_SOURCE,
    CONF_VERSION,
    KEY_CORE,
    KEY_FRAMEWORK_VERSION,
    KEY_TARGET_FRAMEWORK,
    KEY_TARGET_PLATFORM,
)
from esphome.core import CORE, coroutine_with_priority
import esphome.config_validation as cv
import esphome.codegen as cg

from .const import CONF_RESTORE_FROM_FLASH, KEY_BOARD, KEY_ESP8266, esp8266_ns
from .boards import ESP8266_FLASH_SIZES, ESP8266_LD_SCRIPTS

# force import gpio to register pin schema
from .gpio import esp8266_pin_to_code  # noqa


CODEOWNERS = ["@esphome/core"]
_LOGGER = logging.getLogger(__name__)
AUTO_LOAD = ["preferences"]


def set_core_data(config):
    CORE.data[KEY_ESP8266] = {}
    CORE.data[KEY_CORE][KEY_TARGET_PLATFORM] = "esp8266"
    CORE.data[KEY_CORE][KEY_TARGET_FRAMEWORK] = "arduino"
    CORE.data[KEY_CORE][KEY_FRAMEWORK_VERSION] = cv.Version.parse(
        config[CONF_FRAMEWORK][CONF_VERSION]
    )
    CORE.data[KEY_ESP8266][KEY_BOARD] = config[CONF_BOARD]
    return config


def _format_framework_arduino_version(ver: cv.Version) -> str:
    # format the given arduino (https://github.com/esp8266/Arduino/releases) version to
    # a PIO platformio/framework-arduinoespressif8266 value
    # List of package versions: https://api.registry.platformio.org/v3/packages/platformio/tool/framework-arduinoespressif8266
    if ver <= cv.Version(2, 4, 1):
        return f"~1.{ver.major}{ver.minor:02d}{ver.patch:02d}.0"
    if ver <= cv.Version(2, 6, 2):
        return f"~2.{ver.major}{ver.minor:02d}{ver.patch:02d}.0"
    return f"~3.{ver.major}{ver.minor:02d}{ver.patch:02d}.0"


# NOTE: Keep this in mind when updating the recommended version:
#  * New framework historically have had some regressions, especially for WiFi.
#    The new version needs to be thoroughly validated before changing the
#    recommended version as otherwise a bunch of devices could be bricked
#  * For all constants below, update platformio.ini (in this repo)
#    and platformio.ini/platformio-lint.ini in the esphome-docker-base repository

# The default/recommended arduino framework version
#  - https://github.com/esp8266/Arduino/releases
#  - https://api.registry.platformio.org/v3/packages/platformio/tool/framework-arduinoespressif8266
RECOMMENDED_ARDUINO_FRAMEWORK_VERSION = cv.Version(2, 7, 4)
# The platformio/espressif8266 version to use for arduino 2 framework versions
#  - https://github.com/platformio/platform-espressif8266/releases
#  - https://api.registry.platformio.org/v3/packages/platformio/platform/espressif8266
ARDUINO_2_PLATFORM_VERSION = cv.Version(2, 6, 2)
# for arduino 3 framework versions
ARDUINO_3_PLATFORM_VERSION = cv.Version(3, 0, 2)


def _arduino_check_versions(value):
    value = value.copy()
    lookups = {
        "dev": (cv.Version(3, 0, 2), "https://github.com/esp8266/Arduino.git"),
        "latest": (cv.Version(3, 0, 2), None),
        "recommended": (RECOMMENDED_ARDUINO_FRAMEWORK_VERSION, None),
    }

    if value[CONF_VERSION] in lookups:
        if CONF_SOURCE in value:
            raise cv.Invalid(
                "Framework version needs to be explicitly specified when custom source is used."
            )

        version, source = lookups[value[CONF_VERSION]]
    else:
        version = cv.Version.parse(cv.version_number(value[CONF_VERSION]))
        source = value.get(CONF_SOURCE, None)

    value[CONF_VERSION] = str(version)
    value[CONF_SOURCE] = source or _format_framework_arduino_version(version)

    platform_version = value.get(CONF_PLATFORM_VERSION)
    if platform_version is None:
        if version >= cv.Version(3, 0, 0):
            platform_version = ARDUINO_3_PLATFORM_VERSION
        elif version >= cv.Version(2, 5, 0):
            platform_version = ARDUINO_2_PLATFORM_VERSION
        else:
            platform_version = cv.Version(1, 8, 0)
    value[CONF_PLATFORM_VERSION] = str(platform_version)

    if version != RECOMMENDED_ARDUINO_FRAMEWORK_VERSION:
        _LOGGER.warning(
            "The selected Arduino framework version is not the recommended one. "
            "If there are connectivity or build issues please remove the manual version."
        )

    return value


CONF_PLATFORM_VERSION = "platform_version"
ARDUINO_FRAMEWORK_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.Optional(CONF_VERSION, default="recommended"): cv.string_strict,
            cv.Optional(CONF_SOURCE): cv.string_strict,
            cv.Optional(CONF_PLATFORM_VERSION): cv.string_strict,
        }
    ),
    _arduino_check_versions,
)


BUILD_FLASH_MODES = ["qio", "qout", "dio", "dout"]
CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.Required(CONF_BOARD): cv.string_strict,
            cv.Optional(CONF_FRAMEWORK, default={}): ARDUINO_FRAMEWORK_SCHEMA,
            cv.Optional(CONF_RESTORE_FROM_FLASH, default=False): cv.boolean,
            cv.Optional(CONF_BOARD_FLASH_MODE, default="dout"): cv.one_of(
                *BUILD_FLASH_MODES, lower=True
            ),
        }
    ),
    set_core_data,
)


@coroutine_with_priority(1000)
async def to_code(config):
    cg.add(esp8266_ns.setup_preferences())

    cg.add_platformio_option("board", config[CONF_BOARD])
    cg.add_build_flag("-DUSE_ESP8266")
    cg.add_define("ESPHOME_BOARD", config[CONF_BOARD])

    conf = config[CONF_FRAMEWORK]
    cg.add_platformio_option("framework", "arduino")
    cg.add_build_flag("-DUSE_ARDUINO")
    cg.add_build_flag("-DUSE_ESP8266_FRAMEWORK_ARDUINO")
    cg.add_platformio_option(
        "platform_packages",
        [f"platformio/framework-arduinoespressif8266 @ {conf[CONF_SOURCE]}"],
    )
    cg.add_platformio_option(
        "platform", f"platformio/espressif8266 @ {conf[CONF_PLATFORM_VERSION]}"
    )

    # Default for platformio is LWIP2_LOW_MEMORY with:
    #  - MSS=536
    #  - LWIP_FEATURES enabled
    #     - this only adds some optional features like IP incoming packet reassembly and NAPT
    #       see also:
    #  https://github.com/esp8266/Arduino/blob/master/tools/sdk/lwip2/include/lwipopts.h

    # Instead we use LWIP2_HIGHER_BANDWIDTH_LOW_FLASH with:
    #  - MSS=1460
    #  - LWIP_FEATURES disabled (because we don't need them)
    # Other projects like Tasmota & ESPEasy also use this
    cg.add_build_flag("-DPIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH_LOW_FLASH")

    if config[CONF_RESTORE_FROM_FLASH]:
        cg.add_define("USE_ESP8266_PREFERENCES_FLASH")

    # Arduino 2 has a non-standards conformant new that returns a nullptr instead of failing when
    # out of memory and exceptions are disabled. Since Arduino 2.6.0, this flag can be used to make
    # new abort instead. Use it so that OOM fails early (on allocation) instead of on dereference of
    # a NULL pointer (so the stacktrace makes more sense), and for consistency with Arduino 3,
    # which always aborts if exceptions are disabled.
    # For cases where nullptrs can be handled, use nothrow: `new (std::nothrow) T;`
    cg.add_build_flag("-DNEW_OOM_ABORT")

    cg.add_platformio_option("board_build.flash_mode", config[CONF_BOARD_FLASH_MODE])

    if config[CONF_BOARD] in ESP8266_FLASH_SIZES:
        flash_size = ESP8266_FLASH_SIZES[config[CONF_BOARD]]
        ld_scripts = ESP8266_LD_SCRIPTS[flash_size]
        ver = CORE.data[KEY_CORE][KEY_FRAMEWORK_VERSION]

        if ver <= cv.Version(2, 3, 0):
            # No ld script support
            ld_script = None
        if ver <= cv.Version(2, 4, 2):
            # Old ld script path
            ld_script = ld_scripts[0]
        else:
            ld_script = ld_scripts[1]

        if ld_script is not None:
            cg.add_platformio_option("board_build.ldscript", ld_script)
