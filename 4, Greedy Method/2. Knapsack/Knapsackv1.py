"""

===========================================================================
Problem: Calculate the maximum profit a traveler can gain by selling his list
of products.
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
    print('\n◼ Reference - https://youtu.be/oTTzNMHM05I\n')


def ReadProducts():
    # Functions to return a sorting criteria
    def SortingCriteria1(array):
        return array[1]

    # Reading the initial parameters
    info = input('\bEnter a value for the knapsack capacity and the number of objects: ').split()
    k, o = int(info[0]), int(info[1])

    # Reading the information about the objects
    entry = list()
    for i in range(o):
        info = input(f'\nType the weight and the profit of the object [{i + 1}]: ').split()
        w, p = int(info[0]), int(info[1])
        entry.append([w, p])
    print('\b')
    line()
    print('\b')

    # Sorting the array by the profit
    return k, o, sorted(entry, key=SortingCriteria1)


def MaxProfit(k, o, entry):
    max_profit, tot = 0, 0

    for i in range(o - 1, -1, -1):
        weight = entry[i][0]
        if (tot + weight) <= k:
            tot += weight
            max_profit += entry[i][1]

    return max_profit


def main():
    Header()
    k, o, entry = ReadProducts()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe maximum profit that the traveler can earn is {MaxProfit(k, o, entry)}')
    Reference()


main()