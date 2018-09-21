from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        dict = defaultdict(bool)
        for index,num in enumerate(nums):
            if target - num in dict:
                return [dict[target-num],index]
            dict[num] = index

x = Solution()
print(x.twoSum([1,2,3],5))


