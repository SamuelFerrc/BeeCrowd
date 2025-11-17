class Solution(object):
    valores = {}
    def tribonacci(self, n):
       # print(self.valores)
        if n in self.valores:
            return self.valores[n]
        if n <= 2:
            return min(n, 1)
        else:

            self.valores[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n-3)
            return self.valores[n]


print(Solution().tribonacci(0))
print(Solution().tribonacci(1))
print(Solution().tribonacci(2))
print(Solution().tribonacci(3))
print(Solution().tribonacci(4))
