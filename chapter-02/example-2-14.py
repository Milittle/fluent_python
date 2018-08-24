#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# A riddle


def test():
    t = (1, 2, [30, 40])
    # t[2] += [50, 60]   it will be wrong
    t[2] .extend([50, 60]) 

    print(t)
# TypeError: 'tuple' object does not support item assignment

def main():
    test()

if __name__ == '__main__':
    main()