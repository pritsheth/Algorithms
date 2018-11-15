def generatePath(nums, target, index):
    if target == 0:
        return 1

    if index == len(nums):
        return 0

    ans = 0
    for j in range(index, len(nums)):
        # if target + nums[j] >= 0 or target - nums[j] >= 0:
        x = generatePath(nums, target + nums[j], j + 1) + generatePath(nums, target - nums[j], j + 1)
        ans += x

    return ans


def createRecursion(nums, n, target):
    if target == 0:
        return 1

    if n < 0:
        return 0

    # exclude current element + include element with sub/add
    ways = createRecursion(nums, n - 1, target) \
           + createRecursion(nums, n - 1, target - nums[n]) + createRecursion(nums, n - 1, target + nums[n])
    return ways


def getTotalWays(nums, target):
    print(generatePath(nums, target, 0))
    print(createRecursion(nums, len(nums) - 1, target))
    pass


getTotalWays([5, 3, -6, 2], 6)
