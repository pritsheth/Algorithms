class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        cur_low, cur_high = 0, 0
        final_low, final_high = 0, 0
        counter = 0
        cursum, final_sum = 0, 0
        flag = -1

        for i in range(0, len(A)):
            if (A[i] == '0'):
                cursum += 1
                if flag == -1:
                    cur_low = i
                    cur_high = i
                    flag = 1
            else:
                cursum -= 1

            # cursum += counter
            if (0 > cursum):
                cursum = 0
                counter = 0
                # update both current
                flag = -1

            # Store the global L and R
            if (cursum > final_sum):
                final_sum = cursum
                final_low = cur_low
                final_high = cur_high

            cur_high += 1

        print(final_high, final_low)


s = Solution()
s.flip("101")



