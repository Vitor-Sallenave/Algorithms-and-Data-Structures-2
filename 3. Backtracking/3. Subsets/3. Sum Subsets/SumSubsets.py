"""

===========================================================================
Problem: Calculate the number of different subsets from an integer array
which the total target_sum is "target_sum".
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
    s = int(input('Enter a value for the target sum: '))
    array = list(map(int, input('Type the array values: ').split()))
    print('\b')
    line()
    print('\b')
    return s, sorted(array)


def CreateP(size):
    return [0 for _ in range(size)]


def SumSubsets(target_sum, s0, vet, ns, t, P):
    i = t
    n = len(vet)

    # Note that we can prune the recursion tree passing the conditions below.
    # This occurs due to the ordering of the vet.
    while i < n and s0 + vet[i] <= target_sum:
        P[ns] = vet[i]
        s0 += vet[i]

        # We found a solution
        if target_sum == s0:
            print(P[:ns+1])
        else:
            SumSubsets(target_sum, s0, vet, ns + 1, i + 1, P)

        s0 -= vet[i]
        i += 1


def main():
    Header()
    target_sum, vet = ReadData()
    P = CreateP(len(vet))
    Solutions = list()
    SumSubsets(target_sum, 0, vet, 0, 0, P)
    print('\b')
    line()
    print(f'\nThe number of subsets that sum {target_sum} is {len(Solutions)}')


main()
