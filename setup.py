from setuptools import setup, find_packages

setup(
    name='debug-datadirs',
    version='0.1.0',
    packages=find_packages(),
    package_data={'': ['data/**']},
)
