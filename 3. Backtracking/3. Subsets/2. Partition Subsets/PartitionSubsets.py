"""

===========================================================================
Problem: Divide the array into 2 parts assuring that the difference between
them is minimum.
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
    array = list(map(int, input('Type the array values: ').split()))
    print('\b')
    line()
    print('\b')
    return array


def CreateS(size):
    return [0 for _ in range(size)]


def Keep(S, ns):
    print(f'{S[:ns + 1]}\n')


def PartitionSumSubsets(C, s, dif, msmp, ns, t, tot, n, S):
    i = t

    while i <= n and (s + C[i]) < msmp:
        S[ns] = i
        s += C[i]

        if abs(tot - 2 * s) < dif:
            Keep(S, ns)
            dif = abs(tot - 2 * s)
            msmp = max(s, tot - s)

        PartitionSumSubsets(C, s, dif, msmp, ns + 1, i + 1, tot, n, S)
        s -= C[i]
        i += 1


def main():
    Header()
    C = ReadData()
    S = CreateS(len(C))
    PartitionSumSubsets(C, 0, float('inf'), float('inf'), 0, 0, sum(C), len(C), S)
    line()


main()