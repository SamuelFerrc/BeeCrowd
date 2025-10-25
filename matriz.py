matrix = [[0,0,0],
          [0,1,0],
          [0,0,0]]

n = 3
i, j = 1, 1
dir = True  # True → direita, False → esquerda

while 0 <= i < n:
    matrix[i][j] = 1
    print("\n".join(map(str, matrix)))
    print("-----")

    if dir:
        j += 1
        if j == n:
            j = n - 1
            i += 1
            dir = False
    else:
        j -= 1
        if j < 0:
            j = 0
            i += 1
            dir = True

    if i == n:  # chegou no fim
        break
