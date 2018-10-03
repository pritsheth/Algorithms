# Given an array of n integers and a number m, find the maximum possible difference between two sets of m elements chosen from given array.


# Difference of K largest elements and K smallest elements:

import heapq


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = []

        for n in nums:
            self.addToMinHeap(self.nums, n, k)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.addToMinHeap(self.nums, val, self.k)
        return self.nums[0]

    def addToMinHeap(self, min_pq, num, k):
        if len(min_pq) < k:
            heapq.heappush(min_pq, num)
            return

        top = min_pq[0]
        if top < num:
            heapq.heapreplace(min_pq, num)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# K1 smallest number and K2 smallest number : Sum of all in this range
def getSumofRange(nums, k1, k2):
    pass
