def reverse(text):
    words = text.split(" ")
    reverseText = ""
    for w in words:
        reverseText += reverseWord(w)
        reverseText += " "
    print(reverseText)


def reverseWord(word1):
    low, high = 0, len(word1) - 1
    word = list(word1)
    while (low < high):
        temp = word[low]
        word[low] = word[high]
        word[high] = temp
        low += 1
        high -= 1

    return "".join(word)

reverse("Hey hello world")
