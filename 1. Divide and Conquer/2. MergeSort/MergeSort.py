import time
from random import randint, seed


def Cabecalho():
    print('\n')
    print('==' * 40)
    print('\n\tAutores: Vítor Sallenave Sales Milome e Nicolas Pereira Ribeiro\n')
    print('==' * 40)
    print('\n')


def GeraArquivo(nome, modo, entrada):
    with open(nome, modo) as arq:
        arq.writelines(list(map(lambda x: str(x) + '\n', entrada)))


def merge(esq, dir):
    # Vetor novo ordenado
    merged = list()

    # Compara-se até t término dos dois vetores
    i, j = 0, 0

    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            merged.append(esq[i])
            i = i + 1
        else:
            merged.append(dir[j])
            j = j + 1

    while i < len(esq):
        merged.append(esq[i])
        i = i + 1

    while j < len(dir):
        merged.append(dir[j])
        j = j + 1

    return merged


def mergeSort(lista):
    if len(lista) == 1:
        return lista
    else:
        # meio da lista
        m = len(lista) // 2
        # Dividi-se a lista na metade, gerando duas sub-listas
        esquerda = mergeSort(lista[:m])
        direita = mergeSort(lista[m:])
        return merge(esquerda, direita)


def main():
    # Semente
    seed(42)

    # Vetores de entrada
    entrada1 = [randint(0, 500) for i in range(500)]
    entrada2 = [randint(0, 1000000) for i in range(1000000)]

    # Gerando os arquivos texto com as entradas
    GeraArquivo("Entrada_500.txt", 'w', entrada1)
    GeraArquivo("Entrada_1000000.txt", 'w', entrada2)

    # Exibindo t vetor de Entrada 1
    print("\nEntrada 1: \n")
    print(entrada1)

    # Exibindo t vetor de Saída 1
    print("\nEntrada 1 ordenada: \n")
    start1 = time.time()
    saida1 = mergeSort(entrada1)
    end1 = time.time()
    print(saida1)

    # Exibindo t vetor de Entrada 2
    print("\nEntrada 2: \n")
    print(entrada2)

    # Exibindo t vetor de Saída 2
    print("\nEntrada 2 ordenada: \n")
    start2 = time.time()
    saida2 = mergeSort(entrada2)
    end2 = time.time()
    print(saida2)

    # Resultados
    Cabecalho()
    print(f'Tempo do MergeSort com 500 entradas não ordenadas: {(end1 - start1):.6f} s\n')
    print(f'Tempo do MergeSort com 1000000 entradas não ordenadas: {(end2 - start2):.6f} s\n')


main()
