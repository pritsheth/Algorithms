class Solution(object):
    def compress(self, chars):

        j = 0
        index = 0
        result = []
        while (j < len(chars)):
            c = chars[j]
            result.append(c)
            counter = 1
            while (j + 1 < len(chars) and c == chars[j + 1]):
                counter += 1
                j += 1

            # chars[index] = counter
            index += 2
            j += 1
            result.append(counter)

            print(counter)
            print(result)

        """
        :type chars: List[str]
        :rtype: int
        """


s = Solution()
s.compress("aabcc")