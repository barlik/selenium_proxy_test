import os
from setuptools import setup, find_packages

setup(
    name = "seleniun-proxy-test",
    version = "0.0.1",
    packages=find_packages(),
    install_requires=['selenium'],
    include_package_data=True,
)
