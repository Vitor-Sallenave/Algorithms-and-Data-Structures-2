"""

===========================================================================
Problem: Given a string S and a dictionary D, demonstrate if S can be
divided in a sequence of at least one word from D separated by spaces.
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


def CreateDict():
    dictionary = str(input("Let's create our dictionary! Type as many words (patterns) as you want\n\
(separated with spaces): ")).strip().split()
    print('\n')
    line()

    return dictionary


def ShowDict(d):
    print('\nOur dictionary is: \n')
    for i in range(len(d)):
        print(f'{i+1} - {d[i]}')
    print('\b')
    line()


def ReadString():
    string = str(input('\nType a text: '))
    print('\b')
    line()

    return string


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


# worst case: the algorithm will verify the whole dictionary
def VerifySearch(dictionary, size, text):
    if size < 0:
        return False
    else:
        return SearchSub(dictionary[size], text) or VerifySearch(dictionary, size-1, text)


def main():
    Header()
    D = CreateDict()
    ShowDict(D)
    S = ReadString()
    answer = VerifySearch(D, len(D)-1, S)
    if answer:
        print("\nThe string can be separated!")
    else:
        print("\nThe string can't be separated in words from our dictionary!")


main()