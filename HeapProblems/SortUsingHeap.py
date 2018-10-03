#
# Given an array of n elements, where each element is at most k away from its target position,
# devise an algorithm that sorts in O(n log k) time. For example,
# let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.
#  It may be assumed that k < n.
#

import heapq


def getSortedArray(nums, k):
    result = nums[:k + 1]

    # To insert the first K element into heap : Slice the list and use the heapify
    heapq.heapify(result)

    index = 0
    for j in range(k + 1, len(nums)):
        x = heapq.heappop(result)
        nums[index] = x
        index += 1
        heapq.heappush(result, nums[j])

    while result:
        x = heapq.heappop(result)
        nums[index] = x
        index += 1


# getSortedArray([6, 5, 3, 2, 8, 10, 9], 3)

import math

# Get height from N nodes of complete binary tree
def getLog(nums):
    for n in nums:
        print(math.floor(math.log2(n)))


getLog([1, 2, 3, 4, 5, 6, 7, 8])
