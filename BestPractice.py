from collections import defaultdict

A = [1,2,3,4]

# To create the dict of index vs value

dict = {i: A[i]for i in range(len(A))}
print(dict)

# To use the default dict:

d = defaultdict(int)
