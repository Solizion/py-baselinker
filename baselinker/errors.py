from requests.models import Response


class ParametersError(Exception):
    pass


class BaseLinkerError(Exception):

    @staticmethod
    def create(response: Response):
        # todo: parse error response
        return BaseLinkerError(response.content)
