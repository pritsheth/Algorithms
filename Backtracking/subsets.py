class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):

        n = len(A)
        result = []
        for i in range(0, 1 << n):
            list = []
            for j in range(n):
                mask = 1 << j
                if i & mask != 0:
                    list.append(A[j])
            result.append(list)
        return result


#
#
# s = Solution()
# A = [1, 2, 3]
# print(s.subsets(A))
#

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(A, temp, index, N):
            result.append(temp[:])

            for i in range(index, N):
                backtrack(A, temp + [A[i]], index + 1, N)

        backtrack(sorted(nums), [], 0, len(nums))
        return result

    # Remove duplicate :
    def subsetsII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def backtrack(A, temp, index, N):
            result.append(temp[:])

            for i in range(index, N):
                # TODO: add condition
                backtrack(A, temp + [A[i]], index + 1, N)

        backtrack(sorted(nums), [], 0, len(nums))
        return result

    def permu(self, nums):

        result = []

        def back(A, temp, index):
            if index == len(A):
                result.append(A[:])

            for i in range(index, len(A)):
                A[index], A[i] = A[i], A[index]
                back(A, temp, index + 1)
                A[index], A[i] = A[i], A[index]

        back(nums, [], 0)
        return result




s = Solution()
A = [1, 2, 3]
print(s.permu(A))
