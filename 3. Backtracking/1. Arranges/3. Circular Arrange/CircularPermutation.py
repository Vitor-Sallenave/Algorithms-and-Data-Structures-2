"""

===========================================================================
Problem: Calculate the circular arrangements that can be performed using
n elements.
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


def ReadOption():
    option = int(input('\bType "1" in order to build your own array or "2" to use a example one: '))
    print('\b')
    return option


def ReadData(option):
    arr = list()

    if option == 1:
        line()
        arr = list(map(int, input('\nType the array values: ').split()))
    elif option == 2:
        # Example array
        arr = [i for i in range(1, 101)]
    line()
    print('\b')

    return arr


def CreateS(n):
    return [False for _ in range(n)]


def CreateP(n):
    return [-1 for _ in range(n)]


def CircularPermutation(array, np, S, P, Solutions):
    n = len(array) - 1

    for i in range(n):
        if not S[i]:
            # Fill P with this number
            P[np] = array[i]
            # Mark on S that the number was used
            S[i] = True
            # At this moment, a solution was found
            if np == n - 1:
                Solutions.append(P)
                print(f'{P}\n')
            else:
                # Pass to a different element that can be part of the solution
                CircularPermutation(array, np + 1, S, P, Solutions)

            # Avoiding repetitions
            S[i] = False


def main():
    Header()
    array = ReadData(ReadOption())
    n = len(array)
    P = CreateP(n)
    # Fixing the last element, so that we can arrange the remaining elements
    P[n - 1] = n
    S = CreateS(n - 1)
    Solutions = list()
    print(f'→ Circular Arrangements:\n')
    CircularPermutation(array, 0, S, P, Solutions)
    line()
    print(f'\nThere are {len(Solutions)} ways of arranging {len(array)} items in a circular way\n')


main()
