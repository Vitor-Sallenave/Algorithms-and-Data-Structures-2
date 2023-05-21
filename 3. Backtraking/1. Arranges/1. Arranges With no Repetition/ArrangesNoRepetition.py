"""

===========================================================================
Problem: Calculate the number of size "q" arrangements that can be done by
using "n" items with no repetition.
===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\b')


def ReadData():
    n = int(input('Enter a value for n: '))
    q = int(input('Enter a value for q: '))
    print('\b')
    line()
    print('\b')
    return n, q


def CreateS(size):
    return [False for _ in range(size)]


def CreateP(size):
    return [-1 for _ in range(size)]


def Arrange(S, n, q, P, np, Solutions):
    for i in range(n):
        # Verifying if the number was not used
        if not S[i]:
            # Fill P with this number
            P[np] = i
            # Mark on S that the number was used
            S[i] = True
            # At this moment, a solution was found
            if np == q-1:
                Solutions.append(P)
                print(P)
            else:
                # Pass to the next possibility
                Arrange(S, n, q, P, np + 1, Solutions)

            # This part below enables the function to control possible repetitions
            S[i] = False


def main():
    Header()
    n, q = ReadData()
    S = CreateS(n)
    P = CreateP(q)
    Solutions = list()
    Arrange(S, n, q, P, 0, Solutions)
    print('\b')
    line()
    print(f'\nThere are {len(Solutions)} ways of arranging {n} items in a group of size {q}')


main()