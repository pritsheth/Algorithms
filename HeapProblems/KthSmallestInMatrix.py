from queue import PriorityQueue

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        pq = PriorityQueue()

        rows = len(matrix)
        cols = len(matrix[0])

        # count
        for i in matrix[0]:
            pq.put(i)




