# Given two strings string1 and string2, find the smallest substring in string1 containing all characters of string2 efficiently.

from collections import defaultdict


def getSmallestString(text, pat):
    if len(text) < len(pat):
        return -1

    patMap = defaultdict(int)
    for ch in pat:
        patMap[ch] += 1

    textMap = defaultdict(int)

    count = 0
    startIndex = 0
    for i in range(len(text)):
        textMap[text[i]] += 1

        # Check
        if text[i] in patMap and textMap[text[i]] <= patMap[text[i]]:
            count += 1

        # Got matching substring:
        if count == len(pat):

            while text[startIndex] not in patMap or textMap[text[startIndex]] > patMap[text[i]]:
                startIndex += 1
                if (textMap[text[startIndex]] > patMap[text[i]]):
                    textMap[text[startIndex]] -= 1

    print(text[startIndex:count+1])


getSmallestString("this is a test string", "tist")
