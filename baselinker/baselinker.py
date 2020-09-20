import json
from typing import Sequence

import requests
from requests import Response

from .entities import Log, Order
from .errors import BaseLinkerError, ParametersError
from .utils import ResponseParser


class BaseLinker:
    """Http client for api.baselinker.com"""

    def __init__(self, host, token):
        self.host = host
        self.token = token

    def get_journal_list(self, **kwargs) -> Sequence[Log]:
        """
        Method get list of logs

        Keywords:
            last_log_id (int): Return logs newer then log with this id
            logs_types (string[]): Return logs in this types
            order_id (int): Return logs for order with this id

        Returns:
            logs (Log[]): List of Log object
        """

        if len(kwargs) < 1:
            raise ParametersError("One of the fields (last_log_id, logs_types, order_id) is required")

        parser = ResponseParser[Log]

        return parser.list(Log, 'logs', self.request('getJournalList', **kwargs))

    def get_orders(self, **kwargs) -> Sequence[Order]:
        """
        Method get list of orders

        Keywords:
            order_id (int): Return only one of Order object
            date_confirmed_from (int): Date of confirmed orders in unix timestamp
            date_from (int): Date of created orders in unix timestamp
            id_from (int): Start id of orders
            get_unconfirmed_orders (bool): Return orders with unconfirmed
            status_id (int): Return orders in this status id
            filter_email (str): Return order by client email

        Returns:
            orders (Order[]): List of order object
        """

        parser = ResponseParser[Order]

        return parser.list(Order, 'orders', self.request('getOrders', **kwargs))

    def request(self, method: str, **kwargs) -> Response:
        """Send request to baselinker"""
        requests_data = {
            'token': self.token,
            'method': method,
            'parameters': json.dumps(kwargs)
        }
        response = requests.post(self.host, data=requests_data)

        if response.status_code != 200:
            raise BaseLinkerError.create(response)

        return response
