"""

===========================================================================
Problema: Alice tem identificado um comportamento estranho na rede de computadores
de sua casa e suspeita que esteja sendo vítima de um ataque cibernético.
Ela pesquisou um pouco sobre o tema na Internet e viu que uma prática comum
para identificar e responder a tais ataques consiste no monitoramento do
que acontece na rede. Depois disso, Alice viu que a maior parte dos
dispositivos e aplicações que usa em sua rede geram arquivos de log,
onde são registrados diversos eventos, como erros, avisos, e informações
variadas sobre o funcionamento destes dispositivos e aplicações.
Ela resolveu então fazer a coleta e o gerenciamento dos arquivos que contém
esses logs para tentar identificar se, de fato, está sofrendo um ataque.
O problema é que Alice não possui recursos computacionais para realizar
o gerenciamento de todos os arquivos de log produzidos.
Para facilitar sua escolha de quais arquivos tratar, Alice criou um esquema
de classificação dos arquivos de acordo com a criticidade, no qual atribuiu
rótulos aos arquivos de acordo com os seguintes níveis:

“1” - crítico, “2” – alto e “3” – moderado, tal que “1” >crit “2” >crit “3”,

onde “>crit” significa “mais crítico que”. Cada arquivo possui também
um tamanho, que representa o número de registros de eventos no arquivo.
Alice quer processar a maior quantidade de eventos, respeitando o espaço
disponível e priorizando os arquivos mais críticos. Ajude Alice a
identificar o maior número de arquivos que ela consegue tratar.

Entrada:
A entrada consiste de vários casos de teste.
A primeira linha representa o número de casos de teste.
Cada caso de teste consiste de uma linha com dois inteiros,
sendo k correspondente ao espaço máximo para armazenamento dos arquivos
e m o número de arquivos (1 <= m <= 10^5), seguida de m linhas
correspondentes aos arquivos a serem processados com dois inteiros:
criticidade (“1 – crítico, “2” – alto e “3” – moderado) e
tamanho n (1 <= n <= 10^5).

Saída:
A saída corresponde ao número máximo de arquivos que podem ser tratados
por Alice, respeitando sua criticidade e o espaço máximo de
armazenamento dos arquivos.

===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome ©":^75}\n')
    line()
    print('\b')


def ReadData():
    # Functions to return a sorting criteria
    def SortingCriteria1(array):
        return array[0]

    def SortingCriteria2(array):
        return array[1]

    # Sorting the array to apply the greedy method
    def Sort(array):
        array_sorted = sorted(array, key=SortingCriteria2)
        array_sorted = sorted(array_sorted, key=SortingCriteria1, reverse=True)
        return array_sorted

    # Reading the important information
    entry = list()
    k = int(input('Enter a value for the full memory: '))
    m = int(input('Enter a value for the number of files: '))
    for i in range(m):
        info = input(f'\nType the level and the size of the file [{i + 1}]: ').split()
        l, n = int(info[0]), int(info[1])
        entry.append([l, n])
    print('\b')
    line()
    print('\b')

    # Sorting the array by the level
    return k, m, Sort(entry)


def MaxFiles(k, m, entry):
    max_files, tot = 0, 0

    for i in range(m - 1, -1, -1):
        file_size = entry[i][1]
        if tot + file_size <= k:
            tot += file_size
            max_files += 1
        else:
            break

    return max_files


def main():
    Header()
    k, m, entry = ReadData()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe maximum number of files that Alice can treat is {MaxFiles(k, m, entry)}')


main()
