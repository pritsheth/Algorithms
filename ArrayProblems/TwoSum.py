from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        dict = defaultdict(bool)
        for index, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], index]
            dict[num] = index


x = Solution()


# print(x.twoSum([1, 2, 3], 5))


# Find all pairs for given sum

def printPairs(nums, target):
    dict = defaultdict(list)
    for index, n in enumerate(nums):
        if target - n in dict:
            for j in dict[target - n]:
                print(index, j)
        dict[n].append(index)


printPairs([1, 1, 1, 1], 2)
