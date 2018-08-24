#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# Cartesian product in a generator expression.

def cp():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)

def main():
    pass

if __name__ == '__main__':
    main()