import math

while True:

    n = int(input())
    if n == 0:
        break
    custos = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    totalPontos = 0


    def dijkstra(M, inicio):
        global totalPontos
        pontos = 0
        n = len(M)
        dist = [math.inf] * n
        visitado = [False] * n
        # pai = [-1] * n

        dist[inicio] = 0

        for _ in range(n):
            # pega nó não visitado com menor distância
            u = None
            menor = math.inf
            for i in range(n):
                if not visitado[i] and dist[i] < menor:
                    menor = dist[i]
                    u = i

            if u is None:
                break

            visitado[u] = True

            # relaxa arestas
            for v, peso in enumerate(M[u]):
                if peso != 0 and not visitado[v]:
                    if dist[u] + peso + custos[v] < dist[v]:
                        dist[v] = dist[u] + peso + custos[v]
                    #  pai[v] = u

        return dist  # , pai


    menor = math.inf
    escolhido = []
    for i in range(n):
        dist = dijkstra(matrix, i)
        print(dist, sum(dist))
        if sum(dist) < menor:
            menor = sum(dist)
            escolhido = dist
            escolhido[i] = custos[i]
    escolhido.sort()
    s = 0
    valor = 0
   # print(escolhido)
    for v in escolhido:
        print(s+v)
        if (s+v) > 420:
            #valor -= 1
            break
        s += v
        valor += 1
    print(valor, s, escolhido, sum(escolhido))
