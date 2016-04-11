#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.04.2016 11:04:07 CEST
# File:    test.py

from __future__ import division, print_function

from fsc.namespace import *

n = namespace(a=1)
#~ n = ord_namespace(a=1)
print(n)
n.assert_("c")
