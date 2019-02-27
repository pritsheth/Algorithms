from collections import defaultdict


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        start, end, maxi, cnt = 0, 0, 0, 0
        result = []
        dict = defaultdict(int)
        maxi = max(nums[0:k])
        result.append(maxi)
        for i in range(k):
            dict[nums[i]] -= 1

        end = k - 1

        while (end < len(nums) - 1):
            end += 1
            dict[nums[end]] -= 1

            dict[nums[start]] += 1
            start += 1

            if maxi < nums[end]:
                maxi = nums[end]
                result.append(maxi)

            elif dict[maxi] < 0:
                print(maxi)
                result.append(maxi)

        # print(result)
        return result


s = Solution()
s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)