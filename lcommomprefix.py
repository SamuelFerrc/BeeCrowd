class Solution(object):
    def removeDuplicates(self, nums):
        vistos = []
        for i in range(len(nums)):
            if nums[i] not in vistos:
                vistos.append(nums[i])
        nums = vistos
        return  nums

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))