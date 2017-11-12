class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        x = 0
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == " "):
                return x
            x += 1

        return x
