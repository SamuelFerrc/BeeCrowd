import math

matrix = [
    [0,1,0,5],
    [0,0,2,0],
    [0,0,0,3],
    [0,0,0,0]
]

def dijkstra(M, inicio):
    n = len(M)
    dist = [math.inf] * n
    visitado = [False] * n
    pai = [-1] * n

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
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    pai[v] = u

    return dist, pai


dist, pai = dijkstra(matrix, 0)
print("Distâncias:", dist)
print("Pais:", pai)
