from collections import defaultdict


def find_length(str):
    dict = defaultdict(int)
    low, length = 0, 0
    for i in range(len(str)):
        if str[i] in dict and dict[str[i]] >= low:
            low = dict[str[i]] + 1
        dict[str[i]] = i
        length = max(length, i - low + 1)
    return length


print(find_length("abcabcbb"))
