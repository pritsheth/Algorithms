# http://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# http://www.lintcode.com/en/problem/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = -float("INF")

    # do intialization if necessary

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        if number < self.minimum:
            y = 2 * number - self.minimum
            self.minimum = number
            self.stack.append(y)  # Always push 2*x - min when x < min
        else:
            self.stack.append(number)

    # write your code here

    """
    @return: An integer
    """

    def pop(self):
        y = self.stack.pop()
        if y < self.minimum:
            x = self.minimum
            self.minimum = 2 * self.minimum - y  # how to fetch the old min : 2*min - y
            return x
        else:
            return y

    # write your code here
    """
    @return: An integer
    """

    def min(self):
        return self.minimum

        # write your code here
