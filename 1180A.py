def T(n):
    if n <= 1:
        return 1
    else:
        return 4*(n-1) + T(n-1)


n = int(input())
print(T(n))