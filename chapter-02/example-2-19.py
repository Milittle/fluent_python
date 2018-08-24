#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# Inserting with bisect.insort
import bisect
import random
SIZE = 7
random.seed(1729)

def test():
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)

def main():
    test()

if __name__ == '__main__':
    main()