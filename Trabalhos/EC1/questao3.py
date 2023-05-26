from time import time as tempo


def linha():
    print('==' * 40)


def Questao():
    print(f'{"TRABALHO EC1 - QUESTÃO 3":^75}')
    linha()
    print('''
◼ Considere um dado array de inteiros A = [a1,a2, ..., an].
Suponha que exista um índice k tal que o subarray [a1, a2, ..., ak] esteja ordenado
em ordem estritamente crescente e o subarray [ak, ..., an] esteja ordenado
em ordem estritamente decrescente. Escreva um algoritmo de divisão e conquista para
determinar o valor de k.''')


def Observacoes():
    print('''
* Exemplo: [1, 3, 5, 6. LIS, 4, 2] ; k = 3 (número 6. LIS)\n
* Obs1: O algoritmo considera que o usuário irá digitar um vetor ordenado'
conforme foi especificado no enunciado.\n
* Obs2: O algoritmo desenvolvido ( θ(logN) ) é muito rápido  quando aplicado sobre
um vetor pequeno. Por esse motivo, o tempo de execução se torna quase desprezível.\n''')


def Cabecalho():
    print('\n')
    linha()
    Questao()
    Observacoes()
    linha()


def LeVetor():
    # Lê uma string que representa uma sequência de elementos
    vet = input('\nDigite uma sequência de inteiros (forma: a1,a2,...,an): \n').split(',')
    print('\b')
    # Transforma todos os elementos da lista em inteiros
    return list(map(lambda x: int(x), vet))


def PrintaVetor(vet):
    linha()
    print(f'\nVetor (tamanho = {len(vet)}):', end=' ')
    for elem in vet:
        print(f'{elem}', end=' ')
    print('\n')
    linha()


def BuscaK(vet, i, f):
    if i == f:
        return i
    else:
        k = (i + f) // 2
        if vet[k] > vet[k-1] and vet[k] > vet[k+1]:
            return k
        elif vet[k] > vet[k-1]:
            return BuscaK(vet, k + 1, f)
        elif vet[k] > vet[k+1]:
            return BuscaK(vet, i, k)
        else:
            return None


def main():
    Cabecalho()
    vetor = LeVetor()
    PrintaVetor(vetor)
    start = tempo()
    k = BuscaK(vetor, 0, len(vetor) - 1)
    end = tempo()
    if k is None:
        print('\nO vetor inserido não satisfaz a condição imposta pelo exercício')
    else:
        print(f'\nO valor do índice k é {k}, que corresponde ao número {vetor[k]}\n')
        linha()
        print(f'\nO tempo de execução da função para o seu vetor é {end - start:.25f} s\n')


main()