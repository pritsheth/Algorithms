class Solution:
    def isValid(self, s):

        stack = []
        for i in s:
            print(len(stack))
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif (len(stack) > 0) and ((i == ')' and (stack[-1] == '(')) or i == ']' and (
                        stack[-1] == '[') or i == '}' and (stack[-1] == '{')):
                stack.pop()
            else:
                return False

        return len(stack) == 0

        """
        :type s: str
        :rtype: bool
        """

    # Clean and concise !!
    def isValid2(self, s):

        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for ch in s:
            if ch in d:
                stack.append(d[ch])
            elif (len(stack) == 0 or ch != stack.pop()):
                return False

        return len(stack) == 0


s = Solution()
print(s.isValid("(}"))
