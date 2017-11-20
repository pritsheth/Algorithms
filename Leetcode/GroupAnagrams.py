from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        result = []
        for word in strs:
            temp = word
            x = ''.join(sorted(temp))
            d[x].append(word)
        for keys in d:
            result.append(d[keys])

        return result


s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
