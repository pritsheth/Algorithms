def getMaximumOfSubArraySizeK(arr, k):
    maxi = 0
    sum = 0
    for i in range(k):
        sum += arr[i]

    for i in range(k, len(arr)):
        sum += arr[i] - arr[i - k]
        maxi = max(sum, maxi)
    return maxi


print(getMaximumOfSubArraySizeK([11, 4, 2, 10, 23, 3, 1, 0, 20], 4))

# https://leetcode.com/problems/subarray-sum-equals-k/description/
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:

# TODO : Sliding window/ subarray sum
from collections import defaultdict

def subarraySum(nums, k):
    dict = defaultdict(int)
    count, sum = 0, 0
    dict[0] = 1

    for i in range(len(nums)):
        sum += nums[i]
        if sum - k in dict:
            count += dict[sum - k]
        dict[sum] += 1
    print("count is ", count)
    return count

subarraySum([1, 1, 1], 2)


# https://www.programcreek.com/2014/10/leetcode-maximum-size-subarray-sum-equals-k-java/
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
#
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
#
# Example 1:
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)


