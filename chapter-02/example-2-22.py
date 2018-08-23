# author:milittle
# Basic operations with rows and columns in a numpy.ndarray.
import numpy
def test():
    a = numpy.arange(12)
    print(a)
    print(type(a))
    print(a.shape)
    a.shape = 3, 4
    print(a)
    print(a[2])
    print(a[2, 1])
    print(a[:, 1])
    print(a.transpose())

def test1():
    floats = numpy.loadtxt('floats-10M-lines.txt')
    print(floats[-3:])
    floats *= .5
    print(floats[-3:])
    from time import perf_counter as pc
    t0 = pc()
    floats /= 3
    print(pc() - t0)
    numpy.save('floats-10M', floats)
    floats2 = numpy.load('floats-10M.npy', 'r+')
    floats2 *= 6
    print(floats2[-3:])


def main():
    test()

if __name__ == '__main__':
    main()