for i in range(int(input())):
    memo = []
    k,n = (map(int, input().split()))
    v = k-1
    s = int((v*(v+1)/2))
    if n <= k:
        print((n-1)%1000007)
        continue
    newN = n-k
    count = 0
    for i in range(newN):
        memo.append(s)
        s += memo[-1]
        s -= count if count < k else memo[count-k]
        count += 1
    print(memo[(n-k)-1]%1000007)

