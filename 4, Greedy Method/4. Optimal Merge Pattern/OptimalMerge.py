"""

===========================================================================
Problem: Calculate the maximum profit you can generate by solving tasks in
basis in the workload of your company.
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


def Reference():
    print('\b')
    line()
    print('\n◼ Reference - https://youtu.be/HHIc5JZyenI\n')


def ReadFiles():
    # Reading the initial parameter
    f = int(input('\bEnter a value for the number of files: '))

    # Reading the information about the tasks
    entry = list()
    for i in range(f):
        size = int(input(f'\nType the size of the file [{i + 1}]: '))
        entry.append(size)
    print('\b')
    line()
    print('\b')

    # Sorting the entry by the size
    sorted_entry = sorted(entry, reverse=True)

    return f, sorted_entry


def OptimalMerge(f, entry):
    coast = 0

    while len(entry) > 1:
        current_sum = 0
        for _ in range(2):
            current_sum += min(entry)
            entry.pop(entry.index(min(entry)))
        entry.append(current_sum)
        coast += current_sum

    return coast


def main():
    Header()
    f, entry = ReadFiles()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe total coast of merging is {OptimalMerge(f, entry)}')
    Reference()


main()