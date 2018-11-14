from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        d = OrderedDict()

        for index, char in enumerate(s):

            if char in d:
                d[char] = n
            else:
                # TODO: Ordered keys
                d.update({char: index})
                d.move_to_end(char)

        for val in d.values():
            if val == n:
                continue
            return val

        return -1
