import sys

for linha in sys.stdin:
    linha = linha.strip()
    a,b = map(int , linha.split())
    if a < 0 or b<=0:
        break
    lista = list(range(min(a,b), max(a,b)+1))
    print(*lista, f"Sum={sum(lista)}")