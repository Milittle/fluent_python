#!/usr/bin/python
#-*- coding: utf-8 -*-
# author:milittle
# Building lists of lists

def test():
    board = [['_'] * 3 for i in range(3)]

    print(board)
    board[1][2] = 'A'
    print(board)

def main():
    test()

if __name__ == '__main__':
    main()