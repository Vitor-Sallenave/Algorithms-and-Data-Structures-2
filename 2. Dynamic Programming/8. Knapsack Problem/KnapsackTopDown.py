"""

Problem:

Determine the maximum amount that can be carried using a w weight knapsack.
Each item i weights wi and has a vi value.

"""


def line():
    print('==' * 40)


def ReadData():
    print('\n')
    line()
    x = int(input("\nType the knapsack's weight: "))
    y = list(map(lambda e: int(e), input("\nType the items' weights: ").split()))
    z = list(map(lambda e: int(e), input("\nType the items' values: ").split()))
    if len(y) != len(z):
        print("\nERROR! The arrays don't have the same size!\n")
        exit()
    print('\n')

    return x, y, z


def PrintData(a, b):
    print(f'\tYour weights: {a}\n\tYour values: {b}\n')


def CreateMatrix(lin, col):
    return [[-1 for _ in range(col + 1)] for _ in range(lin)]


def PrintMatrix(mat, wghts, vals):
    li, co = len(mat), len(mat[0])

    line()
    print('\nMemory: \n')
    PrintData(wghts, vals)
    for i in range(li):
        l = list()
        for j in range(co):
            l.append(mat[i][j])
        print(f'\t{l}')
    print('\n')
    line()


def Knapsack(w, i, weights, values, memory):
    if w == 0 or i < 0:
        memory[i][w] = 0
    else:
        if memory[i][w] == -1:
            # Is there any space in the knapsack
            if weights[i] <= w:
                # There are two possibilities: add or not the item
                add_item = Knapsack(w - weights[i], i-1, weights, values, memory) + values[i]
                pass_item = Knapsack(w, i-1, weights, values, memory)
                memory[i][w] = max(add_item, pass_item)
            else:
                memory[i][w] = Knapsack(w, i-1, weights, values, memory)

    return memory[i][w]


def main():
    weight, weights, values = ReadData()
    k = len(weights) - 1
    memory = CreateMatrix(k+1, weight)
    answer = Knapsack(weight, k, weights, values, memory)
    PrintMatrix(memory, weights, values)
    print(f'\nThe maximum amount you can carry on your {weight} kg knapsack is {answer}')


main()