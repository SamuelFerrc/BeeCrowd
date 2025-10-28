n, t = map(int, input().split())
precos = []
for i in range(n):
    c, v = map(int, input().split())
    precos.append((c, v))

vetor = [0] * (t + 1)

for i in range(1, t + 1):
    for c, v in precos:
        if c <= i:
            vetor[i] = max(vetor[i], vetor[i - c] + v)

print(vetor[t])
