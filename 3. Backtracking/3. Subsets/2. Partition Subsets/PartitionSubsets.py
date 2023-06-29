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
    return sorted(array)


def CreateS(size):
    return [0 for _ in range(size)]


def PartitionSumSubsets(C, s, dif, max_sum, ns, t, tot, S):
    i = t
    n = len(C)

    # Pruning the recursion tree
    while i < n and (s + C[i]) < max_sum:
        S[ns] = C[i]
        s += C[i]

        # If adding a new element maintains the difference between the 2 subsets less than dif,
        # then it is a possibility
        if abs(tot - 2 * s) < dif:
            print(f'{S[:ns + 1]}\t->\t{list(set(C) - set(S[:ns + 1]))}')
            # Updating the difference
            dif = abs(tot - 2 * s)
            # Updating the max sum between the subsets
            max_sum = max(s, tot - s)

        # Passing to the next possible subset
        PartitionSumSubsets(C, s, dif, max_sum, ns + 1, i + 1, tot, S)

        s -= C[i]
        i += 1


def main():
    Header()
    C = ReadData()
    S = CreateS(len(C))

    # Total sum of the set
    tot = sum(C)

    # Difference between the 2 initial divided subsets
    dif = abs(tot - 2 * C[0])

    # Verifying which part has a greater sum
    max_sum = max(C[0], tot - C[0])

    PartitionSumSubsets(C, C[0], dif, max_sum, 0, 0, tot, S)
    line()


main()