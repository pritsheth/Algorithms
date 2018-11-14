# Sparse Table approach:

def getRangeMinimumQuery(nums):
    dist = [[0] * len(nums) for i in range(len(nums))]

    n = len(nums)

    for i in range(n):
        dist[i][i] = i

    for i in range(n):
        for j in range(i + 1, n):

            if nums[j] < nums[dist[i][j - 1]]:
                dist[i][j] = j
            else:
                dist[i][j] = dist[i][j - 1]

    print(dist)


getRangeMinimumQuery([7, 2, 3, 0, 5, 10, 3, 12, 18])

# Square Root decomposition:




# TODO: Must do the segment tree:
