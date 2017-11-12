class Solution:
    # @param A : list of integers
    # @return a list of integers

    def maxSubArray(self, nums):
        for i in range(len(nums)):
            max_cur = max(0, max(max_cur + nums[i]))
            max_global = max(max_global, max_cur)
        return max_global

    def maxset(self, A):
        cur_sum, final_sum = 0, 0
        current = [0] * 2
        final = [-1] * 2
        flag = -1

        for i in range(len(A)):
            if (A[i] < 0):
                cur_sum = 0
                flag = -1
            else:
                if (flag == -1):
                    current[0] = i
                    current[1] = i
                    flag = 0

                cur_sum += A[i]
                current[1] = i
                if cur_sum >= final_sum:
                    final_sum = cur_sum
                    if final_sum == 0 and final[1] - final[0] > current[1] - current[0]:
                        continue
                    final[0] = current[0]
                    final[1] = current[1]

        if (final[0] == -1 and flag == -1):
            return []
        print(final)
        return A[final[0]:final[1] + 1]


s = Solution()
print(s.maxset(
    [25150, 1412, 82797, 48381, 7065, -47699, -25129, -65483, -64607, -45322, -55176, 27224, 80366, 60444, 70285,
     -93898, -41133, 96576, -58266, 21711, -20614, -95737, 20591, -48762, -76197, -38588, -54873, 37304, 61200, -68960,
     93947]))
print(s.maxset([0, 0, -1, 0]))
