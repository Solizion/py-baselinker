# Python BaseLinker API

py-baselinker is a Python client library for accessing the [BaseLinker](https://baselinker.com/) service.

Currently, **library is BETA version** and testing only on Python version 3.8.

Library not implement each of method from BaseLinker API [Documentation](https://api.baselinker.com/) yet.

## Install

```shell script
pip install py-baselinker
```

## Usage example
### last weeks orders:
```python
from baselinker import BaseLinker
from datetime import datetime

bl = BaseLinker("https://api.baselinker.com/connector.php",'token')
date_from = datetime.strptime('2021-11-01', '%Y-%m-%d').timestamp()
bl.get_orders(date_from=date_from)
order_sources_list = bl.request('getOrderSources').json()['sources']
order_statuses_list = bl.request('getOrderStatusList').json()['statuses']


```

## Versioning 

Versioning is base on [semver](https://semver.org/). 
The new version is release by a new tag.

## Licence

This library is distributed under the BSD 3 Licence, see LICENSE for more information.

## Contributing

Author of this library is [Mikołaj Jeziorny](https://mikolaj-jeziorny.pl).

If you want to help with development it - **fork me!**