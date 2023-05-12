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
    print('\b')


def ReadChange():
    x = int(input('Type the payment value: '))
    print('\b')
    l()
    return x


def T(v, p, n):
    if n < 0 or p < 0:
        return 0
    else:
        if n == 0:
            return 1
        else:
            use_coin = T(v, p, n - v[p])
            pass_coin = T(v, p-1, n)
            return use_coin + pass_coin


def main():
    Header()
    # coins
    v = [1, 5, 10, 25, 50, 100]
    # m coins
    m = len(v)
    n = ReadChange()
    answer = T(v, m-1, n)
    print(f'\nDistinct ways of giving the {n} change with these {m} coins: {answer}\n')


main()