import sys

criancas = []
for linha in sys.stdin:
    linha = linha.strip()
    if linha == '0':
        break
    criancas.append(linha)

criancas.sort(key=str.lower, reverse=True)
print(criancas[0])



