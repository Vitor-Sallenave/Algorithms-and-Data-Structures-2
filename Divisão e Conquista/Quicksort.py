from time import time


def Cabecalho():
    print('\n')
    print('==' * 40)
    print('\n\tAutores: Vítor Sallenave Sales Milome e Nicolas Pereira Ribeiro\n')
    print('==' * 40)
    print('\n')


def LeArquivo(nome, modo):
    with open(nome, modo) as arq:
        vetor = list(map(lambda x: int(x), arq.readlines()))
    return vetor


def Particione(v, a, b):
    """
    :param v: vetor
    :param a: posição inicial
    :param b: posição final
    :return: posição q do vetor tal que A[a...q-1] <= A[q] < A[q+1...b].

    """

    # Pivô -> último elemento do vetor
    pivo = v[b]

    # Percorrendo e ordenando o vetor
    i = a - 1
    for j in range(a, b):
        if v[j] <= pivo:
            i += 1
            aux = v[i]
            v[i] = v[j]
            v[j] = aux

    aux2 = v[i + 1]
    v[i + 1] = v[b]
    v[b] = aux2

    return i + 1


def QuickSort(v, i, f):
    """
    :param v: vetor
    :param i: posição inicial
    :param f: posição final

    """

    if i < f:
        p = Particione(v, i, f)
        QuickSort(v, i, p - 1)
        QuickSort(v, p + 1, f)


def main():
    # Vetores de exemplo
    A = LeArquivo("Entrada_1000000.txt", 'r')
    B = LeArquivo("Entrada_500.txt", 'r')

    # Medição do tempo do QuickSort aplicado a um vetor não ordenado
    start1 = time()
    QuickSort(A, 0, 999999)
    end1 = time()

    start2 = time()
    QuickSort(B, 0, 499)
    end2 = time()

    # Resultados
    Cabecalho()
    print(f'Tempo do QuickSort com 500 entradas NÃO ordenadas: {(end2 - start2):.8f} s\n')
    print(f'Tempo do QuickSort com 1000000 entradas NÃO ordenadas: {(end1 - start1):.8f} s\n')


main()