"""

===========================================================================
Problem:
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


def ReadOption():
    option = int(input('\bType "1" in order to build your own array or "2" to use a example one: '))
    print('\b')
    return option


def ReadData(option):
    arr = list()

    if option == 1:
        line()
        arr = list(map(int, input('\nType the array values: ').split()))
    elif option == 2:
        # Example array
        arr = [i for i in range(1, 101)]

    line()
    print('\b')
    return arr


def CircularPermutation(array):
    if not array:
        return []

    permutations = []

    for i in range(len(array)):
        permutations.append(array[i:] + array[:i])

    return permutations


def main():
    Header()
    array = ReadData(ReadOption())
    answer = CircularPermutation(array)
    print(f'→ Circular Arrangements:\n\n{answer}\n')
    line()
    print(f'\nThere are {len(answer)} ways of arranging {len(array)} items in a circular way\n')


main()
