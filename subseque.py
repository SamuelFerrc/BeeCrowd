memo = {}
for t in range(int(input())):
    tamanho = int(input())
    principal = input().strip()
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
            if anterior > oMeu:
                return

        texto = ''.join(c for idx, c in enumerate(buscando) if idx not in atual)
        if isPalindrome(texto):
            palindrome = atual

        if i < n:
            gera(atual, i + 1, n, buscando)
            gera(atual + [i], i + 1, n, buscando)

    if principal not in memo:
        gera([], 0, tamanho, principal)
        memo[principal] = palindrome
    else:
        palindrome = memo[principal]

    if palindrome != "-1":
        print(len(palindrome))
        novos = [str(int(x)+1) for x in palindrome]
        print(' '.join(novos))
    else:
        print("-1")



