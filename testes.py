tamanho = 0
principal = ["100101"]
#principais = ["111011011"]
listas = []
palindrome = "-1"


def isPalindrome(s):
    return s == s[::-1]


def gera(atual, i, n, buscando):
    global palindrome
    if palindrome != "-1":
        return
    if i > n:
        return
    if len(atual) >= 1 and i < n:
        anterior = int(buscando[atual[-1]])
        oMeu = int(buscando[i])
        # print(anterior, oMeu, atual, "|",atual[-1], buscando[i], i)
        if anterior > oMeu:
            return
    # if atual not in listas:
    # listas.append(atual)

    texto = ''.join(c for idx, c in enumerate(buscando) if idx not in atual)
    if isPalindrome(texto):
        # print(atual)
        palindrome = atual
    #else:
       # return
    # print(listas)
    if i < n:
        gera(atual + [i], i + 1, n, buscando)
        gera(atual, i + 1, n, buscando)


gera([], 0, len(principal), principal)
if palindrome != "-1":
    print(len(palindrome))
    novos = [str(int(x) + 1) for x in palindrome]
    print(' '.join(novos))
else:
    print("-1")


