"""

===========================================================================
Problem: Given two arrays: A e B, you need to determine the minimum
operations number in order to transform A into B.
The possible operations are: insert, delete or exchange a char.
===========================================================================

"""


def l():
    print('==' * 40)


def Header():
    print('\n')
    l()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    l()
    print('\n')


def ReadStrings():
    string1 = str(input('Digite a primeira frase: ')).strip().lower()
    string2 = str(input('Digite a segunda frase: ')).strip().lower()
    print('\n')
    l()

    return string1, string2


def D(ph1, i, ph2, j):
    if i < 0 or j < 0:
        return 0
    else:
        if ph1[i] == ph2[j]:
            return D(ph1, i-1, ph2, j-1)
        else:
            # Possible operations
            deleteA = D(ph1, i-1, ph2, j)
            insertA = D(ph1, i, ph2, j-1)
            exchangeAB = D(ph1, i-1, ph2, j-1)

            return min(deleteA, insertA, exchangeAB) + 1
            

def main():
    Header()
    str1, str2 = ReadStrings()
    x, y = len(str1)-1, len(str2)-1
    print(f'The number of operations to transform the first phrase into the second one is: {D(str1, x, str2, y)}\n')


main()