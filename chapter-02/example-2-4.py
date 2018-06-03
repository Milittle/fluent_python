# author: milittle
# Cartesian products 笛卡儿积

def cartesian_():
    colors = ['red', 'blue']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)


def main():
    cartesian_()

if __name__ == '__main__':
    main()