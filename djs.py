import math

#matrix = [
 #   [0,3,0,5],
  #  [0,0,2,0],
   # [0,0,0,3],
   # [0,0,0,0]
#]

matrix = [
    [0,0,8,6],
    [0,0,2,0],
    [0,0,0,8],
    [0,2,0,0]
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
        print(f"DistA == {dist}")
        for v, peso in enumerate(M[u]):
            print(f"{v,peso}, dist[u] == {dist[u]}, dist[v] == {dist[v]}, dist == {dist[u] + peso}, u == {u}")
            if peso != 0 and not visitado[v]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    pai[v] = u
        print(f"DistD == {dist}")
        print()

    return dist, pai


dist, pai = dijkstra(matrix, 0)
print("Distâncias:", dist)
print("Pais:", pai)
