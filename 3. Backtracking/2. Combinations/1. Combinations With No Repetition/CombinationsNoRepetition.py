"""

===========================================================================
Problem: Calculate the number of size "q" combinations that can be done by
using "n" items without repetition.
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


def Comb(n, q, np, P, Solutions):
    for i in range(1, n + 1):
        # Verifying if the element is greater than the previous one.
        # This strategy avoids combinations like: (a, b) and (b, a), that are the same
        if i > P[np - 1]:
            P[np] = i
            if np == q:
                Solutions.append(P[1:])
                print(f'{P[1:]}\n')
            else:
                Comb(n, q, np + 1, P, Solutions)


def main():
    Header()
    n, q = ReadData()
    P = CreateP(q + 1)
    P[0] = 0
    Solutions = list()
    print('→ Combinations:\n')
    Comb(n, q, 1, P, Solutions)
    line()
    print(f'\nThere are {len(Solutions)} ways of combining {n} items in a group of size {q}')


main()