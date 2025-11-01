class Solution(object):
    def isValid(self, s):
        parents = []
        for c in s:

            if c == "(" or c == "[" or c == "{":
                parents.append(c)
                continue
            else:
                if len(parents) == 0:
                    return False
                if parents[-1] == "(" and c == ")":
                    parents.pop()
                    continue

                elif parents[-1] == "[" and c == "]":
                    parents.pop()
                    continue

                elif parents[-1] == "{" and c == "}":
                    parents.pop()
                    continue
                return False
            #print(parents, c)
        return len(parents) == 0


while True:
    print(Solution().isValid(input().strip()))
