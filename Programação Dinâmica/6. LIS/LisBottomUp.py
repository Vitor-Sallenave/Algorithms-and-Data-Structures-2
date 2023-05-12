def line():
    print('==' * 40)


def ReadData():
    print('\n')
    line()
    v = list(map(lambda x: int(x), str(input('\nType a array: ')).split()))
    print('\n')

    return v


def CreateArray(size):
    return [-1 for _ in range(size)]


def PrintMemory(memo, array):
    line()
    print(f'\nMemory:\n\n\tYour array:\t\t{array}\n\n\tThe results:\t{memo}\n')
    line()


def lis(vet, i, memory):
    # Initializing maximum subsequence
    max_sub = 0

    # Filling the memory
    for a in range(i+1):
        memory[a] = 1
        for b in range(a):
            if vet[b] < vet[a]:
                # There are two possibilities: use or not the number
                use_num = memory[b] + 1
                pass_num = memory[a]
                memory[a] = max(use_num, pass_num)
        max_sub = max(memory[a], max_sub)

    return max_sub, memory


def main():
    arr = ReadData()
    k = len(arr) - 1
    memory = CreateArray(k+1)
    answer, memory = lis(arr, k, memory)
    PrintMemory(memory, arr)
    print(f'\nThe largest crescent sequence has {answer} number(s)')


main()