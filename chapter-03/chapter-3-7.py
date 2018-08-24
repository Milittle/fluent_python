#!/usr/bin/python
#-*- coding: utf-8 -*-

# author:milittle
# StrKeyDict0 converts non-string keys to str on lookup. See tests in example-3-6

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def get(self, key, default=None):
        try:
            return self[key]
        except:
            return default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()