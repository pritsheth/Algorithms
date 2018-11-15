class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)):
            index_ = abs(nums[index])
            if nums[index_] < 0:
                # print(n)
                return abs(index_)
            else:
                nums[index_] = -nums[index_]
                # print(nums[n])


s = Solution()
print(s.findDuplicate([1,2,2]))