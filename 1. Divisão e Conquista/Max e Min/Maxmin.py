# O Seguinte algoritmo tem um enfoque não recursivo, porém usa metodologias referentes à 1. Divisão e Conquista


def cabecalho():
    print('\n')
    print('==' * 30)
    print('\n\tAutor: Vítor Sallenave Sales Milome\n')
    print('==' * 30)
    print('\n')


def MaxMin(v):
    n = len(v)
    vmin = v[n-1]
    vmax = v[n-1]
    
    for i in range(n // 2):
        if v[2*i - 1] < v[2*i]:
            vmin = min(v[2*i - 1], vmin)
            vmax = max(v[2*i], vmax)
        else:
            vmin = min(v[2*i], vmin)
            vmax = max(v[2*i - 1], vmax)

    return (vmin, vmax)


vetor = [2, 4, 1, 9, 16, 23, 12, 29, 0, -1]
r = MaxMin(vetor)
cabecalho()
print(f'\nO máximo e o mínimo valor do vetor são: {r[1]} e {r[0]}\n')
