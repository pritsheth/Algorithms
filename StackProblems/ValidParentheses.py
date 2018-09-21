class Solution(object):

    def isValid(self, s):

        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {'{': '}', '[': ']', '(': ')'}
        for x in s:
            if x in dict:
                stack.append(x)
            else:
                if not stack and stack.pop() != x:
                    return False

        return len(stack) == 0


