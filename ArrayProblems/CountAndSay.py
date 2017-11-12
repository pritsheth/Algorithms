class Solution(object):
    def countAndSay(self, n):
        x = "1"
        while (n != 1):
            index = 0
            y = ""
            while (index <= len(x) - 1):
                freq, nextIndex = self.getFrequencyAndIndex(x, index)
                y += str(freq)
                y += str(x[index])
                index = nextIndex

            x = y
            n -= 1
        return x

    def getFrequencyAndIndex(self, num, i):
        freq = 0
        x = num[i]
        while (i < len(num) and num[i] == x):
            freq += 1
            i += 1
        return freq, i
