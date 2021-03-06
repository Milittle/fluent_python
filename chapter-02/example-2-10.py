#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# Named tuple attributes and methods 

from collections import namedtuple
def test():
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

    print(City._fields)
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(delhi._asdict())

    for key, value in delhi._asdict().items():
        print(key + ':', value)

def main():
    test()

if __name__ == '__main__':
    main()