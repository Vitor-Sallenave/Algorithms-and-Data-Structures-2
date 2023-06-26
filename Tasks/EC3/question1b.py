def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome ©":^75}\n')
    line()
    print('\b')


def ReadData():
    n = int(input("Type a value for n: "))
    print('\b')
    line()
    print('\b')
    return n


def CreateS(n):
    return [False] * (n - 1)


def CreateP(n):
    return [-1 for _ in range(n)]


def CircularPermutation(n, np, S, P, Solutions):
    for i in range(n):
        if not S[i]:
            S[i] = True
            # Fill P with this number
            P[np] = i
            # At this moment, a solution was found
            if np == n - 1:
                Solutions.append(P)
                print(f'{P}\n')
            else:
                # Pass to the next possibility
                CircularPermutation(n, np + 1, S, P, Solutions)
            S[i] = False

        if len(Solutions) == 100:
            break


def main():
    Header()
    n = ReadData()
    P = CreateP(n)
    S = CreateS(n)
    P[n-1] = n
    CircularPermutation(n - 1, 0, S, P, list())


main()