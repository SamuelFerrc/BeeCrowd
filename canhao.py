import sys
input = sys.stdin.readline


def backtrack(pesoAtual, danoAtual, i):
    if pesoAtual > pesoMaximo:
        return False
    if danoAtual >= danoMaximo:
        return True
    if i == len(projeteis):
        return False
    else:
        possivel = backtrack(pesoAtual + projeteis[i][1], danoAtual + projeteis[i][0], i + 1) or backtrack(
            pesoAtual, danoAtual, i + 1)
        return possivel


for t in range(int(input())):
    n = int(input())
    projeteis = []
    for j in range(n):
        projeteis.append(list(map(int,input().split())))
    pesoMaximo = int(input())
    danoMaximo = int(input())
    soma_coluna1 = sum(linha[0] for linha in projeteis)
    dp = [0] * (pesoMaximo + 1)

    for dano, peso in projeteis:
        for p in range(pesoMaximo, peso - 1, -1):
            dp[p] = max(dp[p], dp[p - peso] + dano)
    print(dp)
    if max(dp) >= danoMaximo:
        print("Missao completada com sucesso" if backtrack(0, 0, 0) else "Falha na missao")
    else:
        print("Falha na missao")
    #print("Missao completada com sucesso" if funciona else "Falha na missao")
