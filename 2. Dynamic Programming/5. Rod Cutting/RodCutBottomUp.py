"""



"""

from random import randrange
from math import inf

NEG_INFINITY = -inf


def line():
    print('==' * 40)

def ReadData():
    print('\n')
    line()
    x = int(input("\nType the rod'target_sum size: "))
    print('\b')

    return x


# Price x size
def Table(k):
    return [i + randrange(1, 5) for i in range(k)]


def RodCut(t, n):
    rod = [0 for i in range(n+1)]
    rod[1] = 1

    # Filling rod
    for i in range(2, n+1):
        max_val = NEG_INFINITY
        # Analyzing previous positions and finding the max value
        # t[j] and rod[i-(j+1)] represent the prices of the divided parts
        for j in range(1, i):
            max_val = max(max_val, t[j] + rod[i-(j+1)])
        rod[i] = max_val

    return rod[n]


def main():
    k = ReadData()
    p = Table(k)
    print(f'Prices x Size: {p}')
    print(f'\nThe maximum amount that can be earned by selling a {k} size rod is {RodCut(p, k)}\n')


main()