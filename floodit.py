matriz = [
    [0, 0, 1, 6, 2],
    [3, 0, 2, 9, 5],
    [4, 5, 0, 3, 3],
    [0, 1, 8, 3, 7]
]
l = 4
c = 5


def flood(matriz, corNova, corAtual, x,y, visitado=None):
    if visitado is None:
        visitado = set()
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]) :
        return
    if(x,y) in visitado:
        return
    visitado.add((x,y))
    if matriz[x][y] != corAtual and matriz[x][y] != corNova:
        return
    else:
        matriz[x][y] = corNova
        flood(matriz, corNova, corAtual, x + 1, y, visitado)
        flood(matriz, corNova, corAtual, x - 1, y, visitado)
        flood(matriz, corNova, corAtual, x, y + 1, visitado)
        flood(matriz, corNova, corAtual, x , y-1, visitado)
    return
def contarMonocromatico(matriz):
    cor = matriz[0][0]
    soma = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j] == cor:
                soma +=1
    return soma
maiorValor = 999990
import copy

def backtrack(matriz, passos):
    global maiorValor, l, c

    contagem = contarMonocromatico(matriz)
    if contagem == l * c:
        maiorValor = min(maiorValor, passos)
        return

    # poda: se já tem mais passos que o melhor, corta
    if passos >= maiorValor:
        return

    corAtual = matriz[0][0]

    for corNova in range(10):
        if corNova == corAtual:
            continue  # não muda nada
        nova = copy.deepcopy(matriz)
        flood(nova, corNova, corAtual, 0, 0)
        backtrack(nova, passos + 1)


backtrack(matriz, 0)
print(maiorValor)