#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# Handling missing keys with setdefault

import sys
import re

WORD_RE = re.compile('\w+') # 匹配字母字数

def test():
    index = {}
    with open('./test.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences
    for word in sorted(index, key=str.upper):
        print(word, index[word])

def main():
    test()

if __name__ == '__main__':
    main()