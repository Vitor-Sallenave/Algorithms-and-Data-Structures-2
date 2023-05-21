"""

===========================================================================
Problem: Calculate the number of different subsets from an integer array
which the total sum is "s".
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
    s = int(input('Enter a value for the sum: '))
    array = list(map(int, input('Type the array values: ').split()))
    print('\b')
    line()
    print('\b')
    return s, array


def CreateS(size):
    return [False for _ in range(size)]


def CreateP(size):
    return [0 for _ in range(size)]


def SumSubsets(s, vet_s, s0, vet, P, S):
    for i in range(len(vet)):
        if not S[i]:
            P[i] = vet[i]
            S[i] = True
            if s == s0:
                print(P)
            elif s0 <= s:
                SumSubsets(s, vet_s - vet[i], s0 + vet[i], vet, P, S)
            else:
                SumSubsets(s, vet_s - vet[i], s0, vet, P, S)
            S[i] = False


def main():
    Header()
    s, v = ReadData()
    S = CreateS(len(v))
    P = CreateP(len(v))
    Solutions = list()
    SumSubsets(s, sum(v), 0, v, P, S)
    line()
    print(f'\nThe number of subsets which sums {s} is {len(Solutions)}')


main()