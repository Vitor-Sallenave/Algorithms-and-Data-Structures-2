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
    print('\b')


def ReadStrings():
    string1 = str(input('Digite a primeira frase: ')).strip().lower()
    string2 = str(input('Digite a segunda frase: ')).strip().lower()
    print('\b')
    l()

    return string1, string2


def CreateMatrix(lin, col):
    return [[-1 for _ in range(col)] for _ in range(lin)]


def PrintMatrix(mat):
    li, co = len(mat), len(mat[0])

    l()
    print('\nMemory: \n')
    for i in range(li):
        line = list()
        for j in range(co):
            line.append(mat[i][j])
        print(f'\t{line}')
    print('\b')
    l()


def D(ph1, i, ph2, j, memory):
    if i < 0 or j < 0:
        return 0
    else:
        if ph1[i] == ph2[j]:
            memory[i][j] = D(ph1, i-1, ph2, j-1, memory)
        else:
            # Possible operations
            deleteA = D(ph1, i-1, ph2, j, memory)
            insertA = D(ph1, i, ph2, j-1, memory)
            exchangeAB = D(ph1, i-1, ph2, j-1, memory)

            memory[i][j] = min(deleteA, insertA, exchangeAB) + 1

    return memory[i][j]
            

def main():
    Header()
    str1, str2 = ReadStrings()
    x, y = len(str1)-1, len(str2)-1
    memory = CreateMatrix(x+1, y+1)
    answer = D(str1, x, str2, y, memory)
    print(f'\nThe number of operations to transform the first phrase into the second one is: {answer}\n')


main()