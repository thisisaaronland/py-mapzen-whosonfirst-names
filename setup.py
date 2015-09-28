#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.names',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.names'],
    version='0.02',
    description='Python tools for working with place names in Who\'s On First data',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-names',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-names/releases/tag/v0.02',
    license='BSD')
