def binarySearch(array, low, high, x):
    if low > high:
        return -1

    mid = low + high >> 1
    if (x == array[mid]):
        return mid
    elif x > array[mid]:
        return binarySearch(array, mid + 1, high, x)
    else:
        return binarySearch(array, low, mid - 1, x)


searchIndex = binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 6)
print(searchIndex)


# Find the first occurence of the number = 0 in sorted array !!



def getFirstIndex(array, low, high):
    if low > high:
        return -1

    mid = low + high >> 1

    if (mid - 1 >= 0 and 0 == array[mid] and array[mid - 1] == 1):
        return mid
    elif mid + 1 <= len(array) - 1 and 1 == array[mid] and array[mid + 1] == 0:
        return mid + 1
    elif mid + 1 <= len(array) - 1 and array[mid] == 1 and array[mid] == array[mid + 1]:
        return getFirstIndex(array, mid + 1, high)
    else:
        return getFirstIndex(array, low, mid - 1)


# Find the repeated element in sorted array:



def getRepeatedNumber(array, low, high, median):
    if low > high:
        return -1
    #
    # mid = low + high >> 1
    # # print(mid)
    # if (mid - 1 >= 0 and array[mid] == array[mid - 1]):
    #     return mid
    # elif mid + 1 <= len(array) - 1 and array[mid] == array[mid + 1]:
    #     return mid + 1
    # elif array[mid] >= median:
    #     return getRepeatedNumber(array, mid + 1, high,median)
    # else:
    #     return getRepeatedNumber(array, low, mid - 1,median)


searchIndex = getRepeatedNumber([1, 1,3,4,5], 0, 4,3)
print(searchIndex)


