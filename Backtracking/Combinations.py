def combination(nums):
    def backtrack(result, nums, path, st_index):
        result.append(path[:])

        for i in range(st_index, len(nums)):
            backtrack(result, nums, path + [nums[i]], i + 1)

    result = []
    backtrack(result, nums, [], 0)
    print(result)


combination([1, 2, 3])


# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3] : same number can be choosen multiple times
# ]


class Solution(object):
    def backtrack(self, result, nums, cur, path, start_index):

        if cur < 0:
            return None

        if cur == 0:
            result.append(path[:])
            return None

        for i in range(start_index, len(nums)):
            # same number can be selected multiple times so not updating i
            self.backtrack(result, nums, cur - nums[i], path + [nums[i]], i)

    def combinationSum(self, candidates, target):
        result = []
        # candidates.sort()
        self.backtrack(result, candidates, target, [], 0)
        return result

    #
    # For
    # example, given
    # candidate
    # set[10, 1, 2, 7, 6, 1, 5] and target
    # 8,
    # A
    # solution
    # set is:
    # [
    #     [1, 7],
    #     [1, 2, 5],
    #     [2, 6],
    #     [1, 1, 6]
    # ]

    def subsetSum(self, result, path, nums, target, st_index):

        if target < 0:
            return None

        if target == 0:
            result.append(path[:])

        for i in range(st_index, len(nums)):
            # TODO: To remove duplicate from subsets
            if i > st_index and nums[i] == nums[i - 1]:
                continue

            self.subsetSum(result, path + [nums[i]], nums, target - nums[i], i + 1)
            # or same number can be selected multiple times so not updating i
            # self.backtrack(result, nums, cur - nums[i], path + [nums[i]], i)

    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.subsetSum(result, [], candidates, target, 0)
        return result


s = Solution()
combination_sum = s.combinationSum([2, 3, 6, 7], 7)
combination_sum1 = s.combinationSum2([8, 10, 1, 2, 7, 6, 1, 5], 8)
print(combination_sum)
print(combination_sum1)
