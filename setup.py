from setuptools import setup, find_packages
from setuptools import find_namespace_packages

setup(
    name='debug-datadirs',
    version='0.1.0',
    packages=find_namespace_packages(),
    package_data={'': ['data/**']},
)
