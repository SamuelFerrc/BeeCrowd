import sys

matriz = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0]
]
meta = 4

def backtrack(i,j):
    global meta
    if (i > meta or i < 0) or (j > meta or j < 0):
        return False
    if matriz[i][j] == 1:
        return False
    if j == meta and i == meta and matriz[i][j] == 0:
        return True
    else:
        matriz[i][j] = 1
        found = backtrack(i,j+1) or backtrack(i-1,j) or backtrack(i+1,j) or backtrack(i,j-1)
        matriz[i][j] = 0
        return found


T = int(input())
for _ in range(T):
    matriz = []
    while len(matriz) < 5: 
        linha = input().strip()
        if linha == "":
            continue
        matriz.append(list(map(int, linha.split())))
    meta = 4
    if backtrack(0, 0):
        print("COPS")
    else:
        print("ROBBERS")
