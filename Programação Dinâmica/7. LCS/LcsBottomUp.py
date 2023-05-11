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


def lcs(array1, array2, i, j, memory):
    # Trivial case
    memory[0][0] = 1

    # Filling the memory
    for a in range(i + 1):
        for b in range(j + 1):
            if memory[a][b] == -1:
                if array1[a] == array2[b]:
                    add = memory[a-1][b-1] + 1
                    memory[a][b] = add
                else:
                    pass1 = memory[a-1][b]
                    pass2 = memory[a][b-1]
                    memory[a][b] = max(pass1, pass2)

    return memory[i][j], memory


def main():
    vet1, vet2 = ReadData()
    s1, s2 = len(vet1), len(vet2)
    memory = CreateMatrix(s1, s2)
    answer, memory = lcs(vet1, vet2, s1 - 1, s2 - 1, memory)
    PrintMemory(memory, vet1, vet2)
    print(f'\nThe largest common sequence between the previous arrays measures {answer} in size')


main()