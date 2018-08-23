# author:milittle
# A list with with three references to the same list is useless.

def test():
    weird_board = [['_'] * 3] * 3
    print(weird_board)
    weird_board[1][2] = '0'
    print(weird_board)



def main():
    test()

if __name__ == '__main__':
    main()


'''
example-2-13的问题：
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
每一次row都是同样的引用，所以后续修改一个地方的值，其他地方也会发生变化
example2-12的代码类似：
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
这样才是正确的，每次循环都新创建了row对象

# 第八章会详细讲解这些陷阱

'''