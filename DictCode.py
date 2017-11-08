from collections import defaultdict


def prepareDict(pairs):
    map1 = defaultdict(list)
    map2 = defaultdict(int)

    for x in pairs:
        parent = x[0]
        child = x[1]
        map1[parent].append(child)
        map2[parent] += 1
    print(map1)
    print(map2)


pairs = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]
prepareDict(pairs)





# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
#
# class Solution(object):
#     def guessNumber(self, n):
#
#         low,high = 1, n
#         while (low < high):
#             mid = (low + high) >> 1
#             if (guess(mid) == 0):
#                 return mid
#             elif guess(mid) == -1:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#
#
#
#     """
#     :type n: int
#     :rtype: int
#     """
