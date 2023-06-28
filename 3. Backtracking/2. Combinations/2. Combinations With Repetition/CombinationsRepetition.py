"""

===========================================================================
Problem: Calculate the number of size "q" combinations that can be done by
using "n" items with repetition allowed.
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


def ReadData():
    n = int(input('Enter a value for n: '))
    q = int(input('Enter a value for q: '))
    print('\b')
    line()
    print('\b')
    return n, q


def CreateP(size):
    return [-1 for _ in range(size)]


def Comb(n, q, np, i, P, Solutions):
    for k in range(i, n + 1):
        P[np] = k
        # We find a solution
        if np == q - 1:
            Solutions.append(P)
            print(f'{P}\n')
        else:
            Comb(n, q, np + 1, k, P, Solutions)


def main():
    Header()
    n, q = ReadData()
    P = CreateP(q)
    Solutions = list()
    print('→ Combinations:\n')
    Comb(n, q, 0, 1, P, Solutions)
    line()
    print(f'\nThere are {len(Solutions)} ways of combining {n} items in a group of size {q}')


main()