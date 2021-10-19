import pytest
from aiohttp import web

from aiolookin.error import NoUsableService
from aiolookin.models import Climate, Device, MeteoSensor, Remote
from aiolookin.protocol import IRFormat


class TestGetInfo:
    async def test_successful(
        self, aiohttp_client, lookin_http_protocol, get_info_response
    ):
        async def handler(_):
            return web.json_response(get_info_response)

        app = web.Application()
        app.router.add_get("/device", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        response = await protocol.get_info()

        assert isinstance(response, Device)

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        app = web.Application()
        app.router.add_get("/device", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.get_info()


class TestUpdateDeviceName:
    async def test_successful(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            return web.json_response({"success": "true"})

        app = web.Application()
        app.router.add_post("/device", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.update_device_name(name="new_name")

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        app = web.Application()
        app.router.add_post("/device", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.update_device_name(name="new_name")


class TestGetMeteoSensor:
    async def test_successful(
        self, aiohttp_client, lookin_http_protocol, get_meteo_sensor_response
    ):
        async def handler(_):
            return web.json_response(get_meteo_sensor_response)

        app = web.Application()
        app.router.add_get("/sensors/meteo", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        response = await protocol.get_meteo_sensor()

        assert isinstance(response, MeteoSensor)

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        app = web.Application()
        app.router.add_get("/sensors/meteo", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.get_meteo_sensor()


class TestGetDevices:
    async def test_successful(
        self, aiohttp_client, lookin_http_protocol, get_devices_response
    ):
        async def handler(_):
            return web.json_response(get_devices_response)

        app = web.Application()
        app.router.add_get("/data", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        response = await protocol.get_devices()

        assert response == get_devices_response

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        app = web.Application()
        app.router.add_get("/data", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.get_devices()


class TestGetDevice:
    async def test_successful(
        self, aiohttp_client, lookin_http_protocol, get_device_response
    ):
        async def handler(_):
            return web.json_response(get_device_response)

        _uuid = "49C2"

        app = web.Application()
        app.router.add_get(f"/data/{_uuid}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        response = await protocol.get_device(uuid=_uuid)

        assert response == get_device_response

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        _uuid = "49C2"

        app = web.Application()
        app.router.add_get(f"/data/{_uuid}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.get_device(uuid=_uuid)


class TestGetConditioner:
    async def test_successful(
        self, aiohttp_client, lookin_http_protocol, get_conditioner_response
    ):
        async def handler(_):
            return web.json_response(get_conditioner_response)

        _uuid = "49C2"

        app = web.Application()
        app.router.add_get(f"/data/{_uuid}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        response = await protocol.get_conditioner(uuid=_uuid)

        assert isinstance(response, Climate)

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        _uuid = "49C2"

        app = web.Application()
        app.router.add_get(f"/data/{_uuid}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.get_conditioner(uuid=_uuid)


class TestGetRemote:
    async def test_successful(
        self, aiohttp_client, lookin_http_protocol, get_device_response
    ):
        async def handler(_):
            return web.json_response(get_device_response)

        _uuid = "49C2"

        app = web.Application()
        app.router.add_get(f"/data/{_uuid}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        response = await protocol.get_remote(uuid=_uuid)
        assert isinstance(response, Remote)

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        _uuid = "49C2"

        app = web.Application()
        app.router.add_get(f"/data/{_uuid}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.get_remote(uuid=_uuid)


class TestSendCommand:
    @pytest.mark.parametrize(
        "command",
        (
            "power",
            "poweron",
            "poweroff",
            "mode",
            "mute",
            "volup",
            "voldown",
            "chup",
            "chdown",
            "swing",
            "speed",
            "cursor",
            "menu",
        ),
    )
    async def test_successful(
        self, command, aiohttp_client, lookin_http_protocol, faker
    ):
        async def handler(_):
            return web.json_response({"success": "true"})

        _uuid = "49C2"
        signal = faker.random.choice(["FF", "01"])

        app = web.Application()
        app.router.add_get(
            f"/commands/ir/localremote/{_uuid}{command}{signal}", handler
        )
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.send_command(uuid=_uuid, command=command, signal=signal)

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(self, aiohttp_client, lookin_http_protocol, faker):
        async def handler(_):
            raise web.HTTPRequestTimeout()

        _uuid = "49C2"
        signal = faker.random.choice(["FF", "01"])
        command = "menu"

        app = web.Application()
        app.router.add_get(
            f"/commands/ir/localremote/{_uuid}{command}{signal}", handler
        )
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.send_command(uuid=_uuid, command=command, signal=signal)

    async def test_invalid_command(self, aiohttp_client, lookin_http_protocol, faker):
        async def handler(_):
            return web.json_response({"success": "true"})

        _uuid = "49C2"
        signal = faker.random.choice(["FF", "01"])
        command = faker.word()

        app = web.Application()
        app.router.add_get(
            f"/commands/ir/localremote/{_uuid}{command}{signal}", handler
        )
        test_client = await aiohttp_client(app)
        protocol = lookin_http_protocol(test_client)

        with pytest.raises(ValueError, match=f"{command} this is the invalid command"):
            await protocol.send_command(uuid=_uuid, command=command, signal=signal)


class TestSendIR:
    @pytest.mark.parametrize(
        "ir_format, url", ((IRFormat.ProntoHEX, "prontohex"), (IRFormat.Raw, "raw"))
    )
    async def test_successful(
        self, ir_format, url, aiohttp_client, lookin_http_protocol
    ):
        async def handler(_):
            return web.json_response({"success": "true"})

        codes = "9024 -4512 564 -564 564"

        app = web.Application()
        app.router.add_get(f"/commands/ir/{url}/{codes}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.send_ir(ir_format=ir_format, codes=codes)

    @pytest.mark.xfail(raises=NoUsableService)
    @pytest.mark.parametrize(
        "ir_format, url", ((IRFormat.ProntoHEX, "prontohex"), (IRFormat.Raw, "raw"))
    )
    async def test_timeout(self, ir_format, url, aiohttp_client, lookin_http_protocol):
        async def handler(_):
            return web.HTTPRequestTimeout()

        codes = "9024 -4512 564 -564 564"

        app = web.Application()
        app.router.add_get(f"/commands/ir/{url}/{codes}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.send_ir(ir_format=ir_format, codes=codes)

    @pytest.mark.parametrize("url", ("prontohex", "raw"))
    async def test_invalid_ir_format(
        self, url, aiohttp_client, lookin_http_protocol, faker
    ):
        async def handler(_):
            return web.HTTPRequestTimeout()

        codes = "9024 -4512 564 -564 564"
        ir_format = faker.word()

        app = web.Application()
        app.router.add_get(f"/commands/ir/{url}/{codes}", handler)
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        with pytest.raises(ValueError, match=f"{ir_format} is not a known IRFormat"):
            await protocol.send_ir(ir_format=ir_format, codes=codes)


class TestUpdateConditioner:
    async def test_successful(
        self, aiohttp_client, lookin_http_protocol, get_conditioner_response
    ):
        async def handler(_):
            return web.json_response({"success": "true"})

        climate = Climate(get_conditioner_response)

        app = web.Application()
        app.router.add_get(
            f"/commands/ir/ac/{climate.extra}{climate.to_status}", handler
        )
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.update_conditioner(climate=climate)

    @pytest.mark.xfail(raises=NoUsableService)
    async def test_timeout(
        self, aiohttp_client, lookin_http_protocol, get_conditioner_response
    ):
        async def handler(_):
            return web.HTTPRequestTimeout()

        climate = Climate(get_conditioner_response)

        app = web.Application()
        app.router.add_get(
            f"/commands/ir/ac/{climate.extra}{climate.to_status}", handler
        )
        test_client = await aiohttp_client(app)

        protocol = lookin_http_protocol(test_client)

        await protocol.update_conditioner(climate=climate)
