import sys
for linha in sys.stdin:
    n = int(linha.strip())
    c = list(map(int, input().split()))

    vetor = [0] * n
    for u in range(n - 1):
        for i in range(n - u - 1):
            if i + 1 < n and i + u + 1 < n:
                if u % 2 == 0:
                    vetor[i] = max(c[i] + vetor[i + 1], c[i + u + 1] + vetor[i])
                else:
                    vetor[i] = min(vetor[i + 1], vetor[i])
    print(vetor[0])
