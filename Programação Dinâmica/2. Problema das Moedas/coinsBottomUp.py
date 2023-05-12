"""

===========================================================================
Question: using 'm' coin types from a country, determine in how many ways a
change 'n' can be given.
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


def ReadChange():
    x = int(input('Type the payment value: '))
    print('\b')
    return x


def CreateMatrix(i, j, value):
    m = list()
    while i > 0:
        m.append([value] * j)
        i -= 1

    return m


def PrintMatrix(m):
    li, co = len(m), len(m[0])

    l()
    print('\nMatrix:\n')
    for i in range(li):
        line = list()
        for j in range(co):
            line.append(m[i][j])
        print(f'\t{line}')
    print('\n')
    l()


def Change(v, m, n):
    # Creating a (m+1) X (n+1) matrix filled with -1
    matrix = CreateMatrix(m+1, n+1, -1)

    # Creating a tabular table
    # Start filling it's first line with an empty n+1 size row
    for k in range(n+1):
        matrix[0][k] = 0

    # Then, fulfil it's second line with ones
    for k in range(n+1):
        matrix[1][k] = 1

    # Let's fill out the table
    for i in range(2, m+1):
        for j in range(n+1):
            if j >= v[i - 1]:
                # There are two possibilities: use or not the coin
                use_num = matrix[i][j - v[i-1]]
                pass_num = matrix[i-1][j]
                matrix[i][j] = use_num + pass_num
            else:
                matrix[i][j] = matrix[i-1][j]

    return matrix, matrix[m][n]


def main():
    Header()
    coins = [1, 5, 10, 25, 50, 100]
    m = len(coins)
    n = ReadChange()
    table, answer = Change(coins, m, n)
    PrintMatrix(table)
    print(f'\nThere are {answer} different ways of giving a {n} change with these {m} coins')


main()