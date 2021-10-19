# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sepplotlib']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3,<4.0.0', 'pandas>=1.3.4,<2.0.0']

setup_kwargs = {
    'name': 'sepplotlib',
    'version': '0.1.0',
    'description': 'Separation plots for classification problems',
    'long_description': '# sepplotlib\n\nSeparation plots for classification problems.\n\n## Installation\n\n`pip install sepplotlib` to install.\n\n',
    'author': 'Remco Bastiaan Jansen',
    'author_email': 'r.b.jansen.uu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
