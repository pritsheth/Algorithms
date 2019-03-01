# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.


class Solution(object):

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {0: -1}
        sum = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += nums[i]

            if sum in dict:
                maxi = max(maxi, i - dict[sum])
            else:
                dict[sum] = i

        return maxi
