"""

===========================================================================
Problem: SubString Search.

Verify if a determined string is part
of a longer one.
===========================================================================

"""

#


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


# Knuth-Morris-Pratt:
def KMP(s1, s2):
    pass


def main():
    Header()
    string1, string2 = ReadStrings()
    answer = KMP(string1, string2)
    if answer:
        print('String 1 is a substring of String 2!')
    else:
        print('String 1 is not inserted in String 2!')


main()

