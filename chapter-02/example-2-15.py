# author:milittle
# The unexpected result: item t2 is changed and an exception is raised.

def test():
    pass
    # t[2] 结果会在抛出异常以后修改对象

def main():
    test()

if __name__ == '__main__':
    main()