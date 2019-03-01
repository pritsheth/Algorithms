from collections import defaultdict


# TODO: Best subarray problem
#  Subarray equal K
class Solution1(object):
    def subarraySum(self, nums, k):

        dict = defaultdict(int)
        sum = count = 0
        dict[sum] = 1

        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in dict:
                count += dict[sum - k]
            dict[sum] = dict[sum] + 1

        return count


#  Lc 713
class Solution2(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
