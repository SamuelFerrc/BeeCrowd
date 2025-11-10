class Solution(object):
    def searchInsert(self, nums, target):
        valor = -1
        for i in range(len(nums)):
            if nums[i] == target:
                valor = i
                break
        if valor == -1:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if nums[i] == target:
                    valor = i
                    break
        return valor

