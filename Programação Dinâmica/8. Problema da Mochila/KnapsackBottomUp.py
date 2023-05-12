"""

Problem:

Determine the maximum amount that can be carried using a w weight knapsack.
Each item i weights wi and has a vi value.

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\n')


def ReadData():
    x = int(input("Type the knapsack's weight: "))
    y = list(map(lambda e: int(e), input("\nType the items' weights: ").split()))
    z = list(map(lambda e: int(e), input("\nType the items' values: ").split()))
    if len(y) != len(z):
        print("\nERROR! The arrays don't have the same size!\n")
        exit(-1)
    print('\b')

    return x, y, z


def PrintData(a, b):
    print(f'\nYour weights: {a}\nYour values: {b}')


def CreateMatrix(lin, col):
    return [[-1 for _ in range(col)] for _ in range(lin)]


def PrintMatrix(mat, wghts, vals):
    li, co = len(mat), len(mat[0])

    line()
    PrintData(wghts, vals)
    print('\nMemory: \n')
    for i in range(li):
        l = list()
        for j in range(co):
            l.append(mat[i][j])
        print(f'\t{l}')
    print('\b')
    line()


def Knapsack(w, i, weights, values, memory):
    # Trivial cases
    memory[0] = [0] * (w+1)
    for c in range(i+1):
        memory[c][0] = 0

    # Filling the memory
    for a in range(1, i+1):
        for b in range(1, w+1):
            if weights[a-1] <= b:
                # There are two possibilities: add or not the item
                add_item = values[a-1] + memory[a-1][b - weights[a-1]]
                pass_item = memory[a-1][b]
                memory[a][b] = max(add_item, pass_item)
            else:
                memory[a][b] = memory[a-1][b]

    return memory[i][w], memory


def main():
    Header()
    weight, weights, values = ReadData()
    k = len(weights)
    memo = CreateMatrix(k+1, weight+1)
    answer, memory = Knapsack(weight, k, weights, values, memo)
    PrintMatrix(memory, weights, values)
    print(f'\nThe maximum amount you can carry on your {weight} kg knapsack is {answer}')


main()