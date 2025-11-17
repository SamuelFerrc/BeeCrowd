class Solution(object):
    valores = []

    def backtrack(self, n, values):
        if sum(values) == n:
            self.valores.append(values)
            return
        if sum(values) > n:
            return
        else:
            self.backtrack(n, values + [1])
            self.backtrack(n, values + [2])

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.valores = []
        self.backtrack(n, [])
        return len(self.valores)

print(Solution().climbStairs(3))
print(Solution().climbStairs(3))