tamanho = int(input())
valor = list(map(int, input().split()))

start = -1
f = 0

maior = 0
if tamanho == 1:
    maior = 1
else:
    trocou = True
    for i in range(1, tamanho):
        if valor[i] < valor[i - 1]:
            maior = max(maior, f - start)
            start = i - 1
            # f = i
        f = i
    maior = max(maior, f - start)

print(maior)
