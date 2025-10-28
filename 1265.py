while True:
    # Leitura do caso de teste
    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break

    sons = input().split()
    consultas = list(map(int, input().split()))

    # Letras dos sons (A, B, C, ...)
    letras = [chr(ord('A') + i) for i in range(n)]

    # Responde cada consulta
    for k in consultas:
        tamanho = 1
        total = 0

        # Descobre o tamanho da palavra que contém o k-ésimo som
        while True:
            cont = tamanho * (n ** tamanho)
            if total + cont >= k:
                break
            total += cont
            tamanho += 1

        # k relativo dentro desse tamanho
        k_rel = k - total - 1  # -1 para índice 0

        # Descobre a palavra na base N
        palavra = []
        for _ in range(tamanho):
            palavra.append(k_rel % n)
            k_rel //= n
        palavra = palavra[::-1]  # inverte para a ordem correta

        # Pega o som correspondente à primeira letra
        letra_index = palavra[0]
        print(sons[letra_index])

    print()
