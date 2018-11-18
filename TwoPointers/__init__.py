class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = ['a', 'e', 'i', 'o', 'u']
        ch = [c for c in s]
        low, high = 0, len(ch) - 1
        while low < high:

            while low < high and ch[low] not in vow:
                print("low")
                low += 1

            while low < high and ch[high] not in vow:
                print("high")
                high -= 1

            ch[low], ch[high] = ch[high], ch[low]
            low += 1
            high -= 1

        return ''.join(ch)


s = Solution()
s.reverseVowels('hello')
