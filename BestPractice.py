from collections import defaultdict

A = [1, 2, 3, 4]

# To create the dict of index vs value

dict = {i: A[i] for i in range(len(A))}
print(dict)

# To use the default dict:

d1 = defaultdict(int)
d2 = defaultdict(list)

# for key,value in d1.items() : iteration

# All sorting functions:

A = [10, 11, 12, 1, 0, -1, 8]
A.sort()
# A.sort(reverse=True)
print(A)

# To take input from STDIN:
# 4,4 --> m,n values
print("Enter input")
n, m = [int(x) for x in input().split(' ')]

# How to use counter:

from collections import Counter

a = [1, 2, 2, 2, 2, 1, 1, 1, 3]
counter = Counter(a)
print(counter)


# Always use self.global if want to utilize global var:
class solution:
    def findTilt(self, root):
        # For global variables:
        self.ans = 0

        def _sum(node):
            if not node: return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right

        _sum(root)
        return self.ans

    def combine(self, A):
        res = []

        def back(A):
            res.append(A)

        back(A)


# TODO: To sort the list based on the value of dict:
# Sorted function will always return the tuples.
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_by_value = sorted(x.items(), key=lambda kv: kv[1])
print("huahahaha", sorted_by_value)

# TODO: To sort the list based on the key of dict:

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_by_key = sorted(x.items(), key=lambda kv: kv[0])
print("huahahaha", sorted_by_key)

# TODO: Bisect for binary search:

import bisect

a = [1, 4, 4, 6]
pos = bisect.bisect_left(a, 4, 0, len(a))
print("binary sorted position", pos)

# TODO : How to use cmp in sorted function.
# TODO : How to use use heap sort
# TODO : How to use use ordered dict
# TODO : How to use use defaultdictd
# TODO : How to use use stack and dequeue (pop and popleft())
