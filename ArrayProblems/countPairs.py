from collections import Counter


def countPairs(k, a):
    d = Counter(a)
    dup = 0
    pairs = 0
    for i in range(0, len(a)):
        if a[i] == k - a[i] and a[i] in d and d[a[i]] > 1:
            dup += 1
        elif k - a[i] in d and d[k - a[i]] >= 1:
            pairs += d[k - a[i]]

    total = dup + pairs // 2
    print("total is new ",total)

countPairs(6,[3,3,3])

#  With dfuplicate pair as well
def findPairsWithAllPair(a, k):
    d = Counter(a)
    dup = 0
    pairs = 0
    for i in range(0, len(a)):
        if a[i] == k + a[i] and a[i] in d and d[a[i]] > 1:
            dup += 1
        elif k + a[i] in d and d[k + a[i]] >= 1:
            pairs += d[k + a[i]]


def findPairs(a, k):
    d = Counter(a)
    dup = 0
    pairs = 0
    for i in range(0, len(a)):
        if a[i] == k + a[i] and a[i] in d and d[a[i]] > 1:
            dup += 1
        elif k + a[i] in d and d[k + a[i]] >= 1:
            pairs += 1
            d[k + a[i]] = 0


    print("dup is", dup)
    print("pairs ", pairs)
    print("dict ", d)

findPairs([3, 1, 4, 1, 5], 2)
