import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    valores = list(map(int, input().split()))
    i = 0
    valor = 0
    while valores[-1] != 0:
        if valores[i] <= 0:
            i += 1
            continue
        distTo = 9999999
        pos = 0
        sub = 0

        while valores[i] > 0:
            for j in range(len(valores)):
                if i == j or valores[j] >= 0:
                    continue
                if distTo > (abs(j - i)):
                    distTo = abs(j - i)
                    pos = j
                    sub = min(valores[i], -valores[j])
            valores[i] -= sub
            valores[pos] += sub
            valor += sub * distTo
            distTo = 9999999
        i += 1
    print(valor)