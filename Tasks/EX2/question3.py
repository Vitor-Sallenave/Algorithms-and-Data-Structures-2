"""

===========================================================================
Problem: Return all the subsets of an array "nums". The solution set must
not contain duplicated subsets.
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
    nums = list(map(int, (input('Enter an array: ')).split()))
    print('\b')
    line()
    print('\b')
    return nums


def CreateS(size):
    return [False for _ in range(size)]


def VerifyS(S):
    return (len(S) >= 2) and (max(S) - min(S)) <= 25


def AllSubsets(nums, ns, t, S):
    n = len(nums)

    for i in range(t, n):
        S[ns] = nums[i]
        # Printing the subset built in this step
        if VerifyS(S[:ns + 1]):
            print(S[:ns + 1])
        # Keep creating new subsets until the end
        if i < n:
            AllSubsets(nums, ns + 1, i + 1, S)


def main():
    Header()
    nums = ReadData()
    S = CreateS(len(nums))
    AllSubsets(nums, 0, 0, S)


main()
