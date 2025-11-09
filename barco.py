memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

for i in range(int(input())):
    n = int(input())
    print(f"Fib({n}) = {fib(n)}")