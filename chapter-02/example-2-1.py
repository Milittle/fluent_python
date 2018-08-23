# author: milittle
# List comprehensions and readability

# example-2-1
def read_unicode_from_string():
    symbols = '$¢£¥€¤'
    codes = []
    for s in symbols:
        codes.append(ord(s))
    print(codes)

# example-2-2
def another_call():
    symbols = '$¢£¥€¤'
    codes = []
    codes = [ord(s) for s in symbols]
    print(codes)

def main():
    read_unicode_from_string()

if __name__ == '__main__':
    main()