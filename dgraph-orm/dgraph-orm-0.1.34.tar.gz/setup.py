# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dgraph_orm', 'dgraph_orm.strawberry_helpers']

package_data = \
{'': ['*']}

install_requires = \
['black>=21.9b0,<22.0',
 'devtools>=0.8.0,<0.9.0',
 'fastapi>=0.70.0,<0.71.0',
 'httpx>=0.19.0,<0.20.0',
 'pydantic[dotenv]>=1.8.2,<2.0.0',
 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'dgraph-orm',
    'version': '0.1.34',
    'description': '',
    'long_description': None,
    'author': 'Jeremy Berman',
    'author_email': 'jerber@sas.upenn.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
