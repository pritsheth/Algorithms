def search(A, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(A) == 0:
        return -1
    lo, hi = 0, len(A) - 1
    pivot = 0
    while lo < hi:
        if hi == lo + 1 and A[hi] < A[lo]:
            pivot = hi
            break
        mid = (lo + hi) // 2
        if A[hi] < A[mid]:
            lo = mid
        else:
            hi = mid
    lo = 0
    hi = len(A) - 1
    if A[pivot] == target:
        return pivot
    if target <= A[hi]:
        lo = pivot + 1
    else:
        hi = pivot - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            hi = mid
        else:
            lo = mid + 1

    return -1


a = [1, 3]
search(a, 0)
