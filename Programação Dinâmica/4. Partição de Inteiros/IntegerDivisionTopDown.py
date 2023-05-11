def line():
    print('==' * 40)


def ReadData():
    print('\n')
    line()
    n = int(input('\nType a value for n: '))
    p = int(input('\nType a value for p: '))
    print('\n')

    return n, p


def CreateMatrix(w, h):
    mat = [[-1 for _ in range(w + 1)] for _ in range(h + 1)]

    return mat


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


def DivideInt(p, x):
    if x < 0 or p < 0:
        memo[p][x] = 0
        return 0
    if x == 0:
        memo[p][x] = 1
        return 1
    else:
        if memo[p][x] == -1:
            use_num = DivideInt(x - p, p)
            pass_num = DivideInt(x, p - 1)
            memo[p][x] = use_num + pass_num

    return memo[p][x]


n, p = ReadData()
memo = CreateMatrix(n, p)
answer = DivideInt(p, n)
PrintMatrix(memo)
print(f'\nThe number of ways you can divide {n} is {answer}')