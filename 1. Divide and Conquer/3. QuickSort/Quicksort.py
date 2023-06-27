from time import time


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print('\n\tAuthors: Vítor Sallenave Sales Milome e Nicolas Pereira Ribeiro\n')
    line()
    print('\n')


def LeArquivo(nome, modo):
    with open(nome, modo) as arq:
        v = list(map(lambda x: int(x), arq.readlines()))
    return v


def Partition(v, a, b):
    # Pivô -> último elemento do vetor
    pivo = v[b]

    # Percorrendo e ordenando t vetor
    i = a - 1
    for j in range(a, b):
        if v[j] <= pivo:
            i += 1
            # Troca os valores
            v[i], v[j] = v[j], v[i]

    v[i + 1], v[b] = v[b], v[i + 1]

    return i


def QuickSort(v, i, f):
    if i < f:
        p = Partition(v, i, f)
        QuickSort(v, i, p)
        QuickSort(v, p + 1, f)


def main():
    # Vetores de exemplo
    A = LeArquivo("Entrada_1000000.txt", 'r')
    B = LeArquivo("Entrada_500.txt", 'r')

    # Medição do tempo do 3. QuickSort aplicado a um vetor não ordenado
    start1 = time()
    QuickSort(A, 0, 999999)
    end1 = time()

    start2 = time()
    QuickSort(B, 0, 499)
    end2 = time()

    # Resultados
    Header()
    print(f'Tempo do QuickSort com 500 entradas NÃO ordenadas: {(end2 - start2):.8f} s\n')
    print(f'Tempo do QuickSort com 1000000 entradas NÃO ordenadas: {(end1 - start1):.8f} s\n')


main()