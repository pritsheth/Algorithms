import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.org = nums
        self.aux = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.aux

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        x = len(self.org)
        result = self.org[:]
        var = x
        for i in range(x):
            id = random.randrange(0, var)
            result[id], result[var - 1] = result[var - 1], result[id]
            var -= 1

        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
