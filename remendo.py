j = 0
l = 5
c = 20
T1 = 2
T2 = 3
remendos = [2,5,8,11,15]
while j < l:
    remendosT1 = 0
    remendosT2 = 0

    antT1 = remendos[j]
    antT2 = remendos[j]

    tempT1 = remendos[j]
    tempT2 = remendos[j]
    while (remendos[tempT1] - antT1) <= T1:
        antT1 = remendos[tempT1]
        tempT1 += 1
        print(tempT1, remendos[tempT1], antT1,(remendos[tempT1] - antT1))
    j += 1