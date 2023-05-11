def line():
    print('==' * 40)


def ReadData():
    print('\n')
    line()
    n = int(input('\nType a value for n: '))
    print('\n')

    return n


def CreateMatrix(w, h):
    return [[-1 for _ in range(w + 1)] for _ in range(h + 1)]


def PrintMatrix(mat):
    li, co = len(mat), len(mat[0])

    line()
    print('\nMemory: \n')
    for i in range(li):
        l = list()
        for j in range(co):
            l.append(mat[i][j])
        print(f'\t{l}')
    print('\n')
    line()


def DivideInt(n):
    # Creating the matrix
    memory = CreateMatrix(n, n)

    # Initializing the first column
    for i in range(n + 1):
        memory[i][0] = 1

    # Filling the matrix
    for j in range(1, n + 1):
        # Initializing the first row
        memory[0][j] = 0
        for k in range(1, n + 1):
            if j >= k:
                use_num = memory[k][j - k]
                pass_num = memory[k - 1][j]
                memory[k][j] = use_num + pass_num
            else:
                memory[k][j] = memory[k - 1][j]

    return memory[n][n], memory


def main():
    n = ReadData()
    answer, matrix = DivideInt(n)
    PrintMatrix(matrix)
    print(f'\nThe number of ways you can divide {n} is {answer}')


main()