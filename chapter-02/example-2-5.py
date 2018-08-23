# author: milittle
# Generator expressions
import array


def genexps():
    symbols = '$¢£¥€¤'
    tup = tuple(ord(symbol) for symbol in symbols)
    arr = array.array('I', (ord(symbol) for symbol in symbols))
    print(tup)
    print(arr)

def main():
    genexps()

if __name__ == '__main__':
    main()