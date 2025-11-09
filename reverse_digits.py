class Solution(object):
    def reverse(self, x):
        x = str(x)
        signal = "-" if x[0] == '-' else ''

        newS = ""
        for c in x:
            if c.isdigit():
                newS += c

        reverse = ""
        reverse += signal
        for i in range(len(newS)):
            reverse += newS[-(i+1)]


        revInt = int(reverse)

        if(revInt > (2**31) - 1):
            return 0
        if(revInt < -(2**31)):
            return 0
        return revInt


while True:
    print(Solution().reverse(input().strip()))