"""

Problem:

Determine the largest common sequence between two arrays.

"""


def line():
    print('==' * 40)


def ReadData():
    print('\n')
    line()
    x = input("\nType the items of the first array: ").split()
    y = input("\nType the items of the second array: ").split()
    print('\b')

    return x, y


def PrintData(a, b):
    print(f'\nFirst array: {a}\nSecond array: {b}')


def CreateMatrix(lin, col):
    return [[-1 for _ in range(col)] for _ in range(lin)]


def PrintMemory(mat, arr1, arr2):
    li, co = len(mat), len(mat[0])

    line()
    PrintData(arr1, arr2)
    print('\nMemory: \n')
    for i in range(li):
        l = list()
        for j in range(co):
            l.append(mat[i][j])
        print(f'\t{l}')
    print('\b')
    line()


def lcs(array1, array2, i, j):
    if i == 0 or j == 0:
        memory[i][j] = 1
    else:
        if memory[i][j] == -1:
            if array1[i] != array2[j]:
                # There are two possibilities: pass1 or pass2 and analyse the remaining sequence
                pass1 = lcs(array1, array2, i-1, j)
                pass2 = lcs(array1, array2, i, j-1)
                memory[i][j] = max(pass1, pass2)
            else:
                add = lcs(array1, array2, i - 1, j - 1) + 1
                memory[i][j] = add

    return memory[i][j]


vet1, vet2 = ReadData()
s1, s2 = len(vet1), len(vet2)
memory = CreateMatrix(s1, s2)
answer = lcs(vet1, vet2, s1-1, s2-1)
PrintMemory(memory, vet1, vet2)
print(f'\nThe largest common sequence between the previous arrays measures {answer} in size')
