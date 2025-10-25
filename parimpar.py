import sys
input = sys.stdin.readline
while True:
    a = int(input())
    if a == 0:
        break
    valores = list(map(int, input().split()))

    n = len(valores)
    matriz = [0] * n

    for u in range(1, n):
        for i in range(n - u):
            j = i + u
            if u % 2 == 1:
                matriz[i] = max((pow(0,valores[i]%2))+matriz[i+1], pow(0,valores[j]%2)+matriz[i])
            else:
                matriz[i] = min(matriz[i+1], matriz[i])
    print(matriz[0])
