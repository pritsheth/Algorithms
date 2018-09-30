# ToDo : Most imp binary search : can be used as search index as well!!

def getIndex(nums, target):
    # Note that here we took high as a length of the array

    # For more understanding : here we are using
    # low<high to avoid infite loop as we are setting (high = mid) when we got match
    low, high = 0, len(nums)
    while (low < high): # Very imp condition
        mid = (low + high) >> 1

        if nums[mid] < target:
            low = mid + 1
        # To get the first index of repeated element:
        else:
            high = mid
            # Here we are not using mid-1

    return low

def getRange(nums, target):
    firstIndex = getIndex(nums, target)

    print("first index is", firstIndex)

    if firstIndex == len(nums) or nums[firstIndex] != target:
        return -1

    lastIndex = getIndex(nums, target + 1)
    print("last index is", lastIndex)
    print(lastIndex - firstIndex)


A = [1, 1, 1, 3, 3, 3, 3, 6]


# print(getRange(A, 4))


def binarySearchIterative(nums, target):
    low, high = 0, len(nums) - 1

    while (low <= high):
        mid = (low + high) >> 1

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def binarySearchRecursive(nums, target):
    def recur(nums, low, high, target):

        if low > high:
            return -1

        mid = (low + high) >> 1

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return recur(nums, low, mid - 1, target)
        else:
            return recur(nums, mid + 1, low, target)

    return recur(nums, 0, len(nums) - 1, target)




A = [1, 12, 16, 20]
print("get first index", getIndex(A, 13))

A = [1, 1, 1, 3, 3, 3, 3, 6]
# print("recursion", binarySearchRecursive(A, 1))
