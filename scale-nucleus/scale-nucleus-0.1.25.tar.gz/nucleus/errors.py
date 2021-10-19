import pkg_resources

nucleus_client_version = pkg_resources.get_distribution(
    "scale-nucleus"
).version

INFRA_FLAKE_MESSAGES = [
    "downstream duration timeout",
    "upstream connect error or disconnect/reset before headers. reset reason: local reset",
]


class ModelCreationError(Exception):
    def __init__(self, message="Could not create the model"):
        self.message = message
        super().__init__(self.message)


class ModelRunCreationError(Exception):
    def __init__(self, message="Could not create the model run"):
        self.message = message
        super().__init__(self.message)


class NotFoundError(Exception):
    def __init__(
        self, message="Could not open file. Check the path or if it exists."
    ):
        self.message = message
        super().__init__(self.message)


class DatasetItemRetrievalError(Exception):
    def __init__(self, message="Could not retrieve dataset items"):
        self.message = message
        super().__init__(self.message)


class NucleusAPIError(Exception):
    def __init__(
        self, endpoint, command, requests_response=None, aiohttp_response=None
    ):
        message = f"Your client is on version {nucleus_client_version}. If you have not recently done so, please make sure you have updated to the latest version of the client by running pip install --upgrade scale-nucleus\n"
        if requests_response is not None:
            message += f"Tried to {command.__name__} {endpoint}, but received {requests_response.status_code}: {requests_response.reason}."
            if hasattr(requests_response, "text"):
                if requests_response.text:
                    message += (
                        f"\nThe detailed error is:\n{requests_response.text}"
                    )

        if aiohttp_response is not None:
            status, reason, data = aiohttp_response
            message += f"Tried to {command.__name__} {endpoint}, but received {status}: {reason}."
            if data:
                message += f"\nThe detailed error is:\n{data}"

        if any(
            infra_flake_message in message
            for infra_flake_message in INFRA_FLAKE_MESSAGES
        ):
            message += "\n This likely indicates temporary downtime of the API, please try again in a minute or two"

        super().__init__(message)
