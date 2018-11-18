from collections import Counter


def findMinimumSubstring(text, pat):
    dict = Counter(pat)
    counter = len(pat)
    start = end = head = 0
    mini = float('INF')

    while end < len(text):

        dict[text[end]] -= 1
        if dict[text[end]] >= 0:  # char of pattern exists
            counter -= 1

        end += 1

        while counter == 0:

            if end - start < mini:
                mini = end - start
                head = start

            # Char of pattern exists in current window so invalidate that !!
            if dict[text[start]] >= 0:
                counter += 1

            dict[text[start]] += 1
            start += 1

    if mini == float('INF'):
        return ""
    print(text[head:head + mini])


def findMaximumSubstring(text, pat):
    dict = Counter(pat)
    counter = len(pat)
    start = end = head = 0
    mini = 0

    while end < len(text):

        dict[text[end]] -= 1
        if dict[text[end]] >= 0:
            counter -= 1

        end += 1

        while counter == 0:

            if end - start > mini:
                mini = end - start
                head = start

            # Char of pattern exists in current window so invalidate that !!
            if dict[text[start]] == 0:
                counter += 1

            dict[text[start]] += 1
            start += 1

    if mini == float('INF'):
        return ""
    print(text[head:head + mini])


# findMaximumSubstring("ADOBECODEBANC", "ABC")

from collections import defaultdict


def findSubWithOutRepeatingChar(s):
    start = end = cnt = mini = head = 0
    dict = defaultdict(int)

    while end < len(s):

        dict[s[end]] += 1
        if dict[s[end]] == 2:
            cnt += 1
        end += 1

        while cnt > 0:

            if dict[s[start]] == 2:
                cnt -= 1
            dict[s[start]] -= 1
            start += 1

        if end - start >= mini:
            mini = end - start
            head = start
            print(s[head:head + mini])

    return mini


# findSubWithOutRepeatingChar("ABDEFGABEF")


def findSubWith2DistinctChar(s):
    start = end = cnt = mini = head = 0
    dict = defaultdict(int)

    while end < len(s):

        dict[s[end]] += 1
        if dict[s[end]] == 1:
            cnt += 1
        end += 1

        while cnt > 2:
            if dict[s[start]] == 1:
                cnt -= 1

            dict[s[start]] -= 1
            start += 1

        if end - start >= mini:
            mini = max(mini, end - start)
            print(s[start:start + mini])

    return mini


findSubWith2DistinctChar("abcbbbbcccbdddadacb")
