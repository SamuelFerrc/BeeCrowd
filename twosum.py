nums = [2,7,11,15]
target = 9

memo = {}
for i in range(len(nums)):
    if (target-nums[i]) in memo:
        print([memo[target-nums[i]], i ])
    else:
        memo[nums[i]] = i

print(memo)


class Solution(object):
    def twoSum(self, nums, target):

        memo = {}
        for i in range(len(nums)):
            if (target - nums[i]) in memo:
                return [memo[target - nums[i]], i]
            else:
                memo[nums[i]] = i

