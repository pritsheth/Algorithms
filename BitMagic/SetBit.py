# no of set bits in log n time.

def getCountBit(n):
    count = 0
    while n > 0:
        n = n & n - 1
        print("n is ", n)
        count += 1
    return count


# print(getCountBit(15))


def isUniqueChars(text):
    bitmap = 0
    for ch in text:
        n = ord(ch) - ord('a')
        if (bitmap & 1 << n == 1):
            return False
        bitmap |= 1 << n
    return True

text = "prit abces"


text1 = sorted(text)
print("sorted text is","".join(text1))


print(isUniqueChars("abcdfg"))
# Setting bit at Nth position

n = 4
n |= 1
print("setting the bit at nth location", n)


#  Checking the bit is set or not at Nth position
