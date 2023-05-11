# Implementing the Bottom-Up method in Fibonacci's series


def Fib(k):
    # Trivial cases
    memo.append(1)
    memo.append(1)

    # Keep building an array for memorization
    for i in range(2, k+1):
        memo.append(memo[i-1] + memo[i-2])

    return memo[k]


memo = list()
print('==' * 40)
x = int(input("Which position from Fibonacci's series do you want to know? "))
print('==' * 40)
print(f"The {x}° value from Fibonacci's series is {Fib(x - 1)}")
print('==' * 40)
print(f'Memo filled: {memo}')