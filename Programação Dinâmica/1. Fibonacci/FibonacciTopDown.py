# Implementing the Top-Down method in Fibonacci's series


def CreateMemo(n):
    return [-1 for _ in range(n)]


def Fib(k):
    if k == 1 or k == 0:
        memo[k] = k
    else:
        if memo[k] == -1:
            memo[k] = Fib(k-1) + Fib(k-2)

    return memo[k]


print('==' * 40)
x = int(input("Which position from Fibonacci's series do you want to know? "))
print('==' * 40)
memo = CreateMemo(x+1)
print(f"The {x}° value from Fibonacci's series is {Fib(x)}")
print('==' * 40)
print(f'Memory filled:\n{memo}')
