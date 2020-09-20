import json
from typing import Sequence


class Entity:
    data_ = {}

    def __init__(self, data: dict):
        self.data_ = data
        pass

    def json(self) -> str:
        return json.dumps(self.data_)

    def get_objects_list_(self, class_, key: str):
        if key in self.data_:
            return [class_(e) for e in self.data_[key]]
        return []

    def __getattr__(self, item):
        return self.data_[item]


class Log(Entity):
    """Log with data of event"""

    NEW_ORDER = 1
    DOWNLOAD_FOD = 2
    PAYED_ORDER = 3
    DELETE_OBJECT = 4
    LINK_ORDER = 5

    pass


class Product(Entity):
    """Product with data"""


class Order(Entity):
    """Order with data"""

    def get_products(self) -> Sequence[Product]:
        return self.get_objects_list_(Product, 'products')
