class Solution(object):
    def peakIndexInMountainArray(self, A):
        return self.getPeakIndex(A, 0, len(A) - 1)

    def getPeakIndex1(self, A, low, high):

        if low >= high:
            return -1

        mid = (low + high) >> 1

        if mid + 1 < len(A) and mid - 1 >= 0 and A[mid] > A[mid + 1] and A[mid - 1] < A[mid]:
            return mid

        if A[mid - 1] < A[mid]:
            return self.getPeakIndex1(A, mid + 1, high)
        elif A[mid - 1] > A[mid]:
            return self.getPeakIndex1(A, low, mid - 1)

    def getPeakIndex2(self, A, low, high):

        if low >= high:
            return -1

        mid = (low + high) >> 1

        if A[mid - 1] > A[mid]:
            return self.getPeakIndex2(A, low, mid - 1)
        elif A[mid + 1] > A[mid]:
            return self.getPeakIndex2(A, mid + 1, high)

        return mid

    #  Most optimized part 1
    def peakIndexMountainArray3(self, A):
        l, r = 0, len(A) - 1
        while l < r:  # very imp as we are setting mid to low and high
            mid = (l + r) >> 1
            # Take right
            if A[mid] < A[mid + 1]:
                l = mid
            #  Take left
            elif A[mid - 1] > A[mid]:
                r = mid
            else:
                return mid


s = Solution()
print(s.peakIndexInMountainArray([3, 4, 5, 1]))
