class Solution(object):
    valores = {}

    def fib(self, n):
        if n in self.valores:
            return self.valores[n]
        if n <= 1:
            return 1
        else:
            self.valores[n] = self.fib(n-1) + self.fib(n-2)
            return self.valores[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.valores = {}
        return self.fib(n)


