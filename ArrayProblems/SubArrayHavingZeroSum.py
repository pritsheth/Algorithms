# Print all subarray having sum 0
from collections import defaultdict


# Hint: If we get the sum in hashmap again and we found our subarray.
def printSubArray(nums):
    dict = defaultdict(list)
    sum = 0
    dict[sum].append(-1)
    for index, n in enumerate(nums):
        sum += n
        if sum in dict:
            start_index = dict[sum]
            for i in start_index:
                print(i + 1, index)

        dict[sum].append(index)


printSubArray([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
