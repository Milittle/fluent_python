#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# index.py uses dict.setdefault to fetch and update a list of word occur‐
# rences from the index in a single line Example 3-4

"""Build an index mapping word -> list of occurrences"""

def test():
    import sys
    import re
    WORD_RE = re.compile('\w+')
    index = {}
    # 一般使用这种方式才是正解，为了使得默认的key不报错，应该使用setdefault，而不是使用get方法
    with open('./test.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)
    
    # 按照字母顺序打印
    for word in sorted(index, key=str.upper):
        print(word, index[word])

def main():
    test()

if __name__ == '__main__':
    main()