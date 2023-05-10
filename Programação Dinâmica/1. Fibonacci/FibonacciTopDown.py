# Implementing the Top-Down method in Fibonacci's series


def CreateMemo(n):
    vet = list()

    for i in range(n):
        if i == 0 or i == 1:
            vet.append(1)
        else:
            vet.append(-1)

    return vet


def Fib(k):
    if memo[k] == -1:
        memo[k] = Fib(k-1) + Fib(k-2)
    return memo[k]


print('==' * 40)
x = int(input("Which position from Fibonacci's series do you want to know? "))
print('==' * 40)
memo = CreateMemo(x)
print(f"The {x}° value from Fibonacci's series is {Fib(x - 1)}")
print('==' * 40)
print(f'Memo filled:\n{memo}')
