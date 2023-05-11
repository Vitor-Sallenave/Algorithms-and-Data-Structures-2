def line():
    print('==' * 40)


def ReadData():
    print('\n')
    line()
    v = list(map(lambda x: int(x), str(input('\nType a array: ')).split()))
    print('\n')

    return v


def CreateArray(size):
    return [-1 for _ in range(size + 1)]


def PrintMemory(memo, array):
    line()
    print(f'\nMemory:\n\n\tYour array:\t\t{array}\n\n\tThe results:\t{memo}')


def lis(vet, i):
    # The position is already filled
    if memory[i] != -1:
        return memory[i]

    # The short sequence possible is 1.
    # We can lengthen it by adding numbers from previous positions
    memory[i] = 1

    for j in range(i):
        if vet[j] < vet[i]:
            # There are two possibilities: add or not the number to the sequence
            add_num = lis(vet, j) + 1
            pass_num = memory[i]
            memory[i] = max(add_num, pass_num)

    return memory[i]


arr = ReadData()
k = len(arr) - 1
memory = CreateArray(k)
answer = lis(arr, k)
PrintMemory(memory, arr)
print(f'\nThe largest crescent sequence has {answer} numbers')