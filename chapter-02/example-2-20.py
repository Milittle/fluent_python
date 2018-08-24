#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# Creating, saving and loading a large array of floats.
from array import array
from random import random




def test():
    floats = array('d', (random() for i in range(10**7)))

    print(floats[-1])

    with open('./floats.bin', 'wb') as f:
        floats.tofile(f)
    

    floats2 = array('d')
    with open('./floats.bin', 'rb') as f:
        floats2.fromfile(f, 10**7)
    print(floats2[-1])

    print(floats == floats2)


def main():
    test()

if __name__ == '__main__':
    main()