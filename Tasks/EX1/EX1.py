"""

===========================================================================
Problem: Verify if all the elements from an array V are the same.
===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome ©":^75}\n')
    line()
    print('\b')


def ReadData():
    array = list(map(lambda x: int(x), input('Type your array: ').split()))
    print('\b')
    return array


def PrintArray(array):
    line()
    print(f'\nYour array:\t{array}\n')
    line()


def IsEqual(array, n):
    if n == 1:
        return True
    elif n == 2:
        return array[0] == array[1]
    else:
        left = IsEqual(array[0: n//2], n//2)
        dir = IsEqual(array[n//2: n], n - n//2)
        return left and dir


def main():
    Header()
    V = ReadData()
    PrintArray(V)
    if IsEqual(V, len(V)):
        print(f'\nAll the elements are equal!')
    else:
        print(f"\nThe elements aren't all the same!")


main()