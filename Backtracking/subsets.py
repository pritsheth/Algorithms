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


s = Solution()
A = [1, 2, 3]
print(s.subsets(A))
