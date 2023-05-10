# Problema do corte do bastão: Determinar o valor máximo obtido cortando um bastão e
# vendendo os pedaços (cortes) ou o bastão inteiro.

from random import randrange
from math import inf

NEG_INFINITY = -inf

# Price x size
def TabelaPrecos(k):
    return [i + randrange(1, 5) for i in range(k)]


# Implementação Bottom up
def CorteBastao(t, n):
    bastao = [0 for i in range(n+1)]
    bastao[1] = 1

    # Filling bastao
    for i in range(2, n+1):
        max_val = NEG_INFINITY
        # Analyzing previous positions and finding the max value
        # t[j] and bastao[i-(j+1)] represent the prices of the divided parts
        for j in range(1, i):
            max_val = max(max_val, t[j] + bastao[i-(j+1)])
        bastao[i] = max_val

    return bastao[n]


def main():
    print('==' * 40)
    k = int(input('Digite o tamanho do bastão: '))
    p = [1, 5, 8, 9]
    print('==' * 40)
    print(f'Tabela de preços x tamanho: {p}')
    print('==' * 40)
    print(f'O valor máximo que se consegue obter vendendo um bastão de tamanho {k} é {CorteBastao(p, k)}\n')


main()