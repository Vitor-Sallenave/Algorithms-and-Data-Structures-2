"""

===========================================================================
Problem: SubString Search.

Verify if a determined string is part
of a longer one.
===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\n')


def ReadStrings():
    s1 = str(input('String 1: ')).strip()
    s2 = str(input('String 2: ')).strip()
    print('\n')
    line()

    return s1, s2


# Brute Force Algorithm: worst case, O( len1.(len2 − len1 + 1) ) = O(len1.len2)
def SearchSub(s1, s2):
    # Strings sizes
    len1, len2 = len(s1), len(s2)

    # Searching for an available index value (i) in s2
    for i in range(len2 - len1 + 1):
        # Analyses each character of s1
        for j in range(len1):
            # They are different? Then the remaining chars aren't useful for our analysis
            if s1[j] != s2[i + j]:
                break
            # Verified all the positions, (i) is valid
            if j == (len1 - 1):
                return True

    return False


def main():
    Header()
    string1, string2 = ReadStrings()
    answer = SearchSub(string1, string2)
    if answer:
        print('String 1 is a substring of String 2!')
    else:
        print('String 1 is not inserted in String 2!')


main()

