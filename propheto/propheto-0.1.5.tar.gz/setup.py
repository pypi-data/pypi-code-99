# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['propheto',
 'propheto.deployments',
 'propheto.deployments.aws',
 'propheto.deployments.azure',
 'propheto.deployments.gcp',
 'propheto.model_frameworks',
 'propheto.package',
 'propheto.package.templates.api',
 'propheto.package.templates.api.v1',
 'propheto.package.templates.api.v1.endpoints',
 'propheto.project',
 'propheto.project.configuration',
 'propheto.tracking']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.105,<2.0.0',
 'cloudpickle>=1.6.0,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'tqdm>=4.61.1,<5.0.0',
 'troposphere>=3.0.1,<4.0.0']

setup_kwargs = {
    'name': 'propheto',
    'version': '0.1.5',
    'description': 'Propheto - MLOps Software Platform',
    'long_description': 'Propheto - Open ML Platform \n===========================\n\nPropheto is a flexible, high-performance framework for deploying, managing, and monitoring models. Using Propheto, data scientists can quickly and easily deploy their models as complete, fully functioning microservices. Propheto allows:\n\n- Integration first to support all major data systems, ML frameworks, amd MLOps tools\n- No vendor lock in so you can use all the tools and systems your team needs\n- Real-time or batch prediction endpoints with minimal overhead and maximum parallelism\n- Easy debugging, testing, and versioning for model pipelines\n- Security first architecture with portability across cloud and on-prem environments\n- Open-core but designed for enterprise (automated logging, monitoring, and documentation)\n\nWith only a few simple commands in their IDE (jupyter notebooks, VS Code, Pycharm, etc.) data scientists can deploy models in their cloud architecture with all of the logging, tracking, scaling, and reporting required.\n\nThe Propheto package works with all major system architectures so that it can easily integrate into the production data and software applications and can easily be managed by other DevOps or software engineering resources. However, Propheto also makes it such that data scientists can self-manage these resources without any burden and without working through these other teams.\n\nIt is quick and easy to get up and running with Propheto. Data scientists can install Propheto using tools like pip, conda, and R’s CRAN package library. With a simple authentication import statement, data scientists can then use Propheto’s packages to seamlessly interact with their AWS, GCP, Azure, or other cloud or on-premise system architecture as needed.\n\nReady to get started? checkout our Quickstart guide or `sample notebook\n<https://github.com/Propheto-io/propheto/blob/main/docs/Propheto%20Iris%20Classification.ipynb>`_ to see Propheto in action.\n',
    'author': 'Dan McDade',
    'author_email': 'dan@propheto.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Propheto-io/propheto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
