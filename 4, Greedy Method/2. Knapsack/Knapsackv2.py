"""

===========================================================================
Problem: Calculate the maximum profit a traveler can gain by selling his
list of products. In this problem, consider dividing a product's weight
when it is necessary in order to enhance the profit.
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
        # Here, our interest is the ratio profit/weight
        entry.append([w, round(p/w, 2)])
    print('\b')
    line()
    print('\b')

    # Sorting the array by the level
    return k, o, sorted(entry, key=SortingCriteria1)


def MaxProfit(k, o, entry):
    max_profit, tot = 0, 0

    for i in range(o - 1, -1, -1):
        # Product details
        max_weight = entry[i][0]
        ratio = entry[i][1]
        current_profit = max_weight * ratio

        if (tot + max_weight) <= k:
            tot += max_weight
            max_profit += current_profit
        else:
            weight_left = k - tot
            max_profit += ratio * weight_left
            tot += weight_left

    return max_profit


def main():
    Header()
    k, o, entry = ReadProducts()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe maximum profit that the traveler can earn is {MaxProfit(k, o, entry)}.\n')


main()