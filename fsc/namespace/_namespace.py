#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.04.2016 10:35:03 CEST
# File:    _namespace.py

from __future__ import division, print_function

from collections import OrderedDict

import blessings
tc = blessings.Terminal()
from fsc.formatting import sstr, error_prefix

__all__ = ["namespace", "ord_namespace"]

# Namespaces are one honking great idea -- let's do more of those!
class namespace_hull(object):
    def __getattr__(self, key):
        """
        Forward magic methods, otherwise get key.
        """
        if key.startswith("__") or key.startswith("_OrderedDict"):
            return super(namespace_hull, self).__getattribute__(key)
        return self[key]
    
    def __setattr__(self, key, val):
        """
        Forward magic methods, otherwise set key.
        """
        if key.startswith("__") or key.startswith("_OrderedDict"):
            super(namespace_hull, self).__setattr__(key, val)
        else:
            self[key] = val
    
    def __delattr__(self, key):
        del self[key]
    
    def assert_(self, *args):
        """
        Make sure every key in args are in the namespace.
        
        Args:
            args:  arbitrary number of keys (str) that needs to be in the namespace.
    
        Returns:
            None
        
        Raises:
            ValueError: in case some keys are missing.
        """
        res = list(set(args).difference(set(self.keys())))
        
        if len(res) != 0:
            ep = error_prefix(self)
            formstr = ep + tc.red("Keys ")+tc.red_bold("{}") + tc.red(" are missing!")
            if len(res) == 1:
                formstr = ep + tc.red("Key ")+tc.red_bold("{}") + tc.red(" is missing!")
            
            raise ValueError(formstr.format(", ".join(res)))
    
    def _print_item(self, key):
        shortstr = sstr(self[key])
        return tc.green_bold("{:<10}".format(key)) + " = " + tc.green(shortstr)
        
    def __str__(self):
        res = []
        
        items = self.items()
        if self._sorted_print:
            items = sorted(items)
        
        for k, v in items:
            res.append(self._print_item(k))
        return  "\n".join(res)

namespace =     type("namespace",     (namespace_hull, dict)       , dict(_sorted_print = True ))
ord_namespace = type("ord_namespace", (namespace_hull, OrderedDict), dict(_sorted_print = False))
