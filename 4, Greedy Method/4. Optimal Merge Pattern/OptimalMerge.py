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

    # Reading the information about the files
    entry = list()
    for i in range(f):
        size = int(input(f'\nType the size of the file [{i + 1}]: '))
        entry.append(size)
    print('\b')
    line()
    print('\b')

    # Sorting the entry by the size
    sorted_entry = sorted(entry, reverse=True)

    return sorted_entry


def OptimalMerge(entry):
    coast = 0

    while len(entry) > 1:
        combined_sum = 0

        # Calculating the combined sum
        for i in range(2):
            combined_sum += entry[i]

        # Removing the combined elements
        entry.pop(0)
        entry.pop(0)

        # Creating new nodes
        entry.append(combined_sum)

        coast += combined_sum

    return coast


def main():
    Header()
    entry = ReadFiles()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe total coast of merging is {OptimalMerge(entry)}')
    Reference()


main()