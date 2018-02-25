# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]



class Solution(object):
    def backtrack(self, result, nums, cur, path, start_index):

        if cur < 0:
            return None

        if cur == 0:
            result.append(path[:])
            return None

        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtrack(result, nums, cur - nums[i], path, i)
            del path[-1]

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

    def backtrackSum(self, result, path, nums, target, st_index):

        if target < 0:
            return None

        if target == 0:
            result.append(path[:])

        for i in range(st_index, len(nums)):
            path.append(nums[i])
            self.backtrackSum(result, path, nums, target - nums[i], i + 1)
            del path[-1]

    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.backtrackSum(result, [], candidates, target, 0)
        return result


s = Solution()
combination_sum = s.combinationSum([2, 3, 6, 7], 7)
combination_sum1 = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(combination_sum)
print(combination_sum1)
