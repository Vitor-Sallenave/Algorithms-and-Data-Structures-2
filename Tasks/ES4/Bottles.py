"""

===========================================================================
Problem: Suponha que voce é proprietário de uma farmácia de manipulações
e possui w comprimidos produzidos de um mesmo tipo de n frascos vazios.
Seja {p1, p2, ..., pn} o número de comprimidos que cada frasco pode conter.
Escreva um algoritmo guloso que, dados w e {p1, p2, ..., pn}, determine o
menor número de frascos necessários para armazenar comprimidos. Prove que
seu algoritmo está correto.
===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\b')


def ReadData():
    w = int(input('Enter a value for the number of pills: '))
    p = sorted(list(map(int, input('\nType the values for the bottles: ').split())))
    print('\b')
    line()
    print('\b')
    return w, p


def Bottles(w, p):
    b, tot = 0, 0
    for i in range(len(p) - 1, -1, -1):
        if tot < w:
            tot = tot + p[i]
            b += 1
        else:
            break

    return b


def Theorem():
    line()
    print(''' 
Para qualquer conjunto p, ao escolhermos, primeiramente, o frasco de maior armazenamento, estamos garantindo que
que o frasco escolhido possui o maior armazenamento possível.

Se considerarmos um conjunto de frascos escolhidos E, de modo que essa solução seja ótima,
ao tentarmos adicionar um novo elemento "e" a esse conjunto, sendo "e" o frasco com maior capacidade possível,
teremos um novo conjunto E', que, por sua vez, contém E.

Em relação a esse novo conjunto, podemos afirmar que ele também configura uma solução ótima, uma vez que,
como mencionado anteriormente, "e" era o maior frasco possível e E representa uma solução também ótima.
    ''')
    line()


def main():
    Header()
    w, p = ReadData()
    print(f'\bThe minimum number of bottles that is needed in order to keep the pills is: {Bottles(w, p)}\n')
    Theorem()


main()