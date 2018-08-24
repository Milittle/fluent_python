#!/usr/bin/python
#-*- coding: utf-8 -*-
# author: milittle
# index.py uses dict.setdefault to fetch and update a list of word occur‐
# rences from the index in a single line Example 3-4.

import re
import collections
import sys

WORD_RE = re.compile('\w+')

def test():
    index = collections.defaultdict(list) #用什么作为默认类型，当键值不存在的时候，就会创建一个list，返回list的引用
    with open('./test.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index[word].append(location)
    

    # print in alphabetical order
    for word in sorted(index, key=str.upper):
        print(word, index[word])

def main():
    test()

if __name__ == '__main__':
    main()