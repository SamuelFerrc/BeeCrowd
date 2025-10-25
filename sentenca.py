while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    sentencas = []
    for i in range(n):
        sentencas.append(input().strip())
    for i in range(n):
        valores = sentencas[i].split()
        a = int(valores[1])
        b = valores[3] == "true."

        if a == (i+1):
            if b:
                soma += 1

        outros_valores = sentencas[a-1].split()
        c = valores[3] == "true."
        if b == c:
            soma +=1
    print(soma)
