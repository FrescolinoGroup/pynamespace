#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    30.03.2016 00:29:06 CEST
# File:    setup.py

import sys

from setuptools import setup

pkgname = 'namespace'
pkgname_qualified = 'fsc.' + pkgname

with open('doc/description.txt', 'r') as f:
    description = f.read()
try:
    with open('doc/README', 'r') as f:
        readme = f.read()
except IOError:
    readme = description

with open('version.txt', 'r') as f:
    version = f.read().strip()

requirements = ['blessings', 'fsc.export', 'fsc.formatting']
if sys.version_info < (3,):
    requirements.append('fsc')

setup(
    name=pkgname_qualified,
    version=version,
    packages=[
        pkgname_qualified
    ],
    url='http://frescolinogroup.github.io/frescolino/pynamespace/' + '.'.join(version.split('.')[:2]),
    include_package_data=True,
    author='C. Frescolino',
    author_email='frescolino@lists.phys.ethz.ch',
    install_requires=requirements,
    description=description,
    long_description=readme,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    license='Apache',
)
