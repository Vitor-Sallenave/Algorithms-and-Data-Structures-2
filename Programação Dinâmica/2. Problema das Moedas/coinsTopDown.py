"""

===========================================================================
Question: using 'm' coin types from a country, determine in how many ways a
change 'n' can be given.
===========================================================================

"""


def l():
    print('==' * 40)


def Header():
    print('\n')
    l()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    l()
    print('\n')


def T(v, p, n):
    if n < 0 or p < 0:
        return 0
    else:
        if n == 0:
            return 1
        else:
            return T(v, p, n - v[p]) + T(v, p-1, n)


def main():
    Header()
    # coins
    v = [1, 5, 10, 25, 50, 100]
    # m coins
    m = len(v)
    n = int(input('Type the payment value: '))
    print('\n')
    l()
    answer = T(v, m-1, n)
    print(f'Distinct ways of giving the {n} change with these {m} coins: {answer}\n')


main()