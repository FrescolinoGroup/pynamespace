#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.04.2016 10:35:03 CEST
# File:    _namespace.py

from __future__ import division, print_function

from collections import OrderedDict

import blessings
#~ from fsc.formatting import sstr, error_prefix
from fsc.export import export
from fsc.formatting import shorten

tc = blessings.Terminal()

# Namespaces are one honking great idea -- let's do more of those!
class NamespaceHull(object):
    def __getattr__(self, key):
        """
        Forward magic methods, otherwise get key.
        """
        if key.startswith("__") or key.startswith("_OrderedDict"):
            return super(NamespaceHull, self).__getattribute__(key)
        return self[key]

    def __setattr__(self, key, val):
        """
        Forward magic methods, otherwise set key.
        """
        if key.startswith("__") or key.startswith("_OrderedDict"):
            super(NamespaceHull, self).__setattr__(key, val)
        else:
            self[key] = val

    def __delattr__(self, key):
        del self[key]

    def assert_existence(self, *attributes):
        """
        Make sure every key in attributes is in the namespace.

        attributes:
            attributes:  arbitrary number of keys (str) that needs to be in the namespace.

        Returns:
            None

        Raises:
            ValueError: in case some keys are missing.
        """
        res = list(set(attributes).difference(set(self.keys())))

        if res:
            ep = error_prefix(self)
            formstr = ep + tc.red("Keys ")+tc.red_bold("{}") + tc.red(" are missing!")
            if len(res) == 1:
                formstr = ep + tc.red("Key ")+tc.red_bold("{}") + tc.red(" is missing!")

            raise ValueError(formstr.format(", ".join(res)))

    def __str__(self):
        keys = list(self.keys())
        if not isinstance(self, OrderedDict):
            keys = sorted(keys)

        max_key_len = max(len(k) for k in keys)
        format_str = '{t.green_bold}{:<' + str(max_key_len) + '}{t.normal} = {t.green}{}{t.normal}'

        res = []
        for k in keys:
            res.append(format_str.format(k, self[k], t=tc))
        return  "\n".join(res)

Namespace = export(type("Namespace", (NamespaceHull, dict), dict()))
OrderedNamespace = export(type("OrderedNamespace", (NamespaceHull, OrderedDict), dict()))
