#!/usr/bin/python
#-*- coding: utf-8 -*-
# author: milittle
# Listcomps versus map and filter

def map_filter():
    symbols = '$¢£¥€¤'
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    beyond_ascii_mf = list(filter(lambda c : c > 127, map(ord, symbols)))
    print(beyond_ascii)
    print(beyond_ascii_mf)


def main():
    map_filter()

if __name__ == '__main__':
    main()
