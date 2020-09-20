from typing import Generic, TypeVar, Sequence

from requests.models import Response

from .errors import BaseLinkerError

T = TypeVar('T')


class ResponseParser(Generic[T]):
    """Interface with methods to parse response from baselinker"""

    @staticmethod
    def check_response(response) -> dict:
        data = response.json()

        if 'status' not in data:
            raise TypeError('Response is bad')

        if 'SUCCESS' != data['status']:
            raise BaseLinkerError.create(response)

        return response.json()

    @staticmethod
    def list(class_, key, response: Response) -> Sequence[T]:
        data = ResponseParser.check_response(response)

        return [class_(e) for e in data[key]]
