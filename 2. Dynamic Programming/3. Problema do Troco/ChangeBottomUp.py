"""

===========================================================================
Problem: You need to give a change (n) using fewer coins (m) as possible.
===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\n')


def CreateMemory(q, p):
    return [[-1 for _ in range(q+1)] for _ in range(p)]


def PrintMemory(memo):
    li, co = len(memo), len(memo[0])

    line()
    print('\nMemory:\n')
    for i in range(li):
        l = list()
        for j in range(co):
            l.append(memo[i][j])
        print(f'\t{l}')
    print('\n')
    line()


def Change(n, c):
    # Initializing the matrix with the basic occasion: 0
    for i in range(m):
        memory[i][0] = 0

    # Filling the array
    for i in range(m):
        for j in range(n+1):
            if c[i] > j:
                memory[i][j] = memory[i-1][j]
            else:
                pass_coin = memory[i - 1][j]
                get_coin = memory[i][j - c[i]] + 1
                memory[i][j] = min(pass_coin, get_coin)

    return memory[m][n]


Header()
# Coins available
coins = [1, 5, 10, 25, 40, 100]
# Number of coins
m = len(coins)
x = int(input('How much does your change costs? '))
# Creating a m X (x+1) size matrix
memory = CreateMemory(m, x)
# Printing the answer and the memory
answer = Change(x, coins)
PrintMemory(memory)
print(f'The lowest coins number that you can use to pay the R$ {x},00 change is: {answer}')