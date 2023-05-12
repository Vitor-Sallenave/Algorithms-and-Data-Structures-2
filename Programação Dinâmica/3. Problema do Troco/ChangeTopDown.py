"""

===========================================================================
Problem: You need to give a change (n) using fewer coins (m) as possible.
===========================================================================

"""


def l():
    print('==' * 40)


def Header():
    print('\n')
    l()
    print(f'\n{"Author: Vítor Sallenave Sales Milome ©":^75}\n')
    l()
    print('\n')


def ReadChange():
    return int(input('How much does your change costs? '))


def CreateMemory(n):
    return [-1 for _ in range(n+1)]


def PrintArray(array):
    print('\n')
    l()
    print('\nMemory: \n\n- Change: ')
    for i in range(len(array)):
        print(f'{i:^3}', end='')
    print(f'\n\n- Minimum coins:\n{array}\n')
    l()


def Change(n, coin_index):
    if n == 0:
        memory[n] = 0
        return 0
    if n < 0:
        return float('inf')
    if coin_index == m:
        return float('inf')

    # if there is an empty space
    if memory[n] == -1:
        # There are two possibilities: use or not the coin
        get_coin = 1 + Change(n - coins[coin_index], coin_index)
        pass_coin = Change(n, coin_index + 1)
        memory[n] = min(get_coin, pass_coin)

    return memory[n]


Header()
# Coins available
coins = [1, 5, 10, 25, 40, 100]
# Number of coins
m = len(coins)
# Change value
x = ReadChange()
# Creating the memory
memory = CreateMemory(x)
# Printing the answer and the memory view
answer = Change(x, 0)
PrintArray(memory)
print(f'\nThe lowest coins number that you can use to pay the R$ {x},00 change is: {answer}')