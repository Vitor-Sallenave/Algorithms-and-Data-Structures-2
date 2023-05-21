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


def AllSubsets(nums, i, subset, solutions):
    # We found a solution
    if i >= len(nums):
        solutions.append(subset.copy())
    else:
        # Including the number
        subset.append(nums[i])
        AllSubsets(nums, i + 1, subset, solutions)

        # Not including the number
        subset.pop()
        AllSubsets(nums, i + 1, subset, solutions)


def main():
    Header()
    nums = ReadData()
    subset, solutions = list(), list()
    AllSubsets(nums, 0, subset, solutions)
    print(f'\bThe subsets ({len(solutions)}) are: {solutions}')


main()