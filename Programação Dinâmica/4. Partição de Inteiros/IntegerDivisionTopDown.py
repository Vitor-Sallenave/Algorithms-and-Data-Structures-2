"""

Problem:

Determine in how many ways you can separate an int n. For instance,
n = 3 -> (1, 1, 1); (1, 2); (3) = 3 ways

"""


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
    return [[-1 for _ in range(w)] for _ in range(h)]


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


def DivideInt(p, x, memo):
    if x < 0 or p < 0:
        memo[p][x] = 0
    if x == 0:
        memo[p][x] = 1
    else:
        if memo[p][x] == -1:
            use_num = DivideInt(x - p, p, memo)
            pass_num = DivideInt(x, p - 1, memo)
            memo[p][x] = use_num + pass_num

    return memo[p][x], memo


def main():
    n, p = ReadData()
    memory = CreateMatrix(n+1, p+1)
    answer, memory = DivideInt(p, n, memory)
    PrintMatrix(memory)
    print(f'\nThe number of ways you can divide {n} is {answer}')


main()