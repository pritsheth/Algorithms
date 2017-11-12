class Solution(object):
    def maxSubArray(self, nums):
        max_cur, max_global = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_cur = max_cur + nums[i]
            max_cur = max(nums[i], max_cur)
            max_global = max(max_global, max_cur)
        return max_global