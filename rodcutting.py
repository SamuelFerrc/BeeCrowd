matriz = [
    [1, 1],
    [2, 5],
    [3, 8],
    [4, 9],
    [5, 10],
    [6, 17],
    [7, 17],
    [8, 20]
]

vetor = [0] * len(matriz)
#vetor[1] = matriz[1][1]
maior = 0

for j in range(len(matriz)):
    q = 0
    for i in range(j):
        q = max(q, matriz[i][1] + vetor[j - i - 1])
    vetor[j] = q
print(vetor)