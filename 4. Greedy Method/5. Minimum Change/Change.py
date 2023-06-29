"""

===========================================================================
Problem: Calculate the minimum quantity of coins that is needed to give a
change. Remember that you must choose a coins set that follows the greedy
methods requirements (e.g Brazil'target_sum coins).
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


def ReadCoins():
    # Reading the initial parameter
    info = input('\bEnter a value for the number of coins and the total change: ').split()
    c, change = int(info[0]), int(info[1])

    # Reading the information about the coins
    entry = list()
    for i in range(c):
        entry.append(int(input(f'\nType the coin value [{i + 1}]: ')))
    print('\b')
    line()
    print('\b')

    # Sorting the entry by the value
    sorted_entry = sorted(entry)

    return sorted_entry, change


def Change(entry, change):
    coins, tot = 0, 0

    for i in range(len(entry) - 1, -1, -1):
        value = entry[i]

        # Verifying if the coin value can be used
        if (tot + value) <= change:
            used_coins = (change - tot) // value
            tot += used_coins * value
            coins += used_coins

    return coins


def main():
    Header()
    entry, change = ReadCoins()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe number of coins used in the change was: {Change(entry, change)}')


main()