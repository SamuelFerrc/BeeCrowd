for t in range(int(input())):
    n, k = map(int, input().split())
    valores = list(map(int, input().split()))
    # valores.sort()

    # print(valores)

    soma = 0
    usou = False
    i =0
    for v in valores:
        if usou:
            usou = False
            continue
        if v == 0:
            i += 1
        else:
            i = 0
        if i == k:
            soma += k/1
            i = 0
            usou = True

    print(soma)