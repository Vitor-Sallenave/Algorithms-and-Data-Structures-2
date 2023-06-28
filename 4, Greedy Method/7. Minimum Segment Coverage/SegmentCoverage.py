"""

===========================================================================
Problem: Given two points a, b and a set of segments, verify if such set
can cover the interval [a, b].
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


def ReadSegments():
    # Functions to return a sorting criteria
    def SortingCriteria(array):
        return array[0]

    # Reading the initial parameters
    s = int(input('\bEnter a value for the number of segments: '))
    interval = input('\bEnter the interval: ').split()
    a, b = int(interval[0]), int(interval[1])

    # Reading the information about the segments
    entry = list()
    for i in range(s):
        info = input(f'\nType the start and the end of the segment [{i + 1}]: ').split()
        s, e = int(info[0]), int(info[1])
        entry.append([s, e])
    print('\b')
    line()
    print('\b')

    # Sorting the entry by the start
    sorted_entry = sorted(entry, key=SortingCriteria)

    return sorted_entry, a, b


def Coverage(entry, a, b):
    segments, x, y = 0, a, 0

    for i in range(len(entry)):
        # The segment was selected
        if entry[i][0] > x:
            x = entry[y][1]
            segments += 1

            # Verifying if the interval was overtaken
            if x >= b:
                break
            elif entry[i][1] > entry[y][1]:
                # Comparing the new element with the one that has the current max end
                y = i

    return segments


def main():
    Header()
    entry, a, b = ReadSegments()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe minimum number of segments needed is: {Coverage(entry, a, b)}')


main()