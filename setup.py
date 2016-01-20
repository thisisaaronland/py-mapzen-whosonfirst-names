#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.names.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.names',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.names'],
    version=version,
    description='Python tools for working with place names in Who\'s On First data',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-names',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-names/releases/tag/' + version,
    license='BSD')
