import sys


def max_pontos_alberto(cartas):
    n = len(cartas)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = cartas[i]
    for i in range(n - 1):
        dp[i][i + 1] = max(cartas[i], cartas[i + 1])

    for tamanho in range(3, n + 1):
        for i in range(n - tamanho + 1):
            j = i + tamanho - 1
            esquerda = cartas[i] + min(dp[i + 2][j] if i + 2 <= j else 0, dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            direita = cartas[j] + min(dp[i + 1][j - 1] if i + 1 <= j - 1 else 0, dp[i][j - 2] if i <= j - 2 else 0)
            dp[i][j] = max(esquerda, direita)

    return dp[0][n - 1]


# Leitura via stdin
for linha in sys.stdin:
    n = int(linha.strip())
    valores = list(map(int, input().split()))
    print(max_pontos_alberto(valores))
