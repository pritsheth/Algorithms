# no of set bits in log n time.

def getCountBit(n):
    count = 0
    while n > 0:
        n = n & n - 1
        print("n is ", n)
        count += 1
    return count


# print(getCountBit(15))
# String is having all unique characters or not

def isUniqueChars(text):
    bitmap = 0
    for ch in text:
        n = ord(ch) - ord('a')
        if (bitmap & 1 << n == 1):
            return False
        bitmap |= 1 << n
    return True


def isOnly1BitSet(bitmap):
    return bitmap & bitmap - 1 == 0


# String permutation :  https://leetcode.com/articles/palindrome-permutation/
def isPalindromePermutation(text):
    bitmap = 0
    for ch in text:
        bitmap = toggleNthBitOptimizeWay(bitmap, ord(ch) - ord('a'))
    return isOnly1BitSet(bitmap)


# Toggle the bit at n th location
def toggleNthBit(bitmap, n):
    mask = 1 << n
    if bitmap & mask == 0:
        bitmap |= mask  # Setting the bit at nth location
    else:
        bitmap &= ~(1 << n)
    return bitmap


def toggleNthBitOptimizeWay(bitmap, n):
    mask = 1 << n
    bitmap ^= mask  # Setting the bit at nth location
    return bitmap


print("toggle the vlaue of bitmap", isPalindromePermutation("aaccf"))

#  Checking the bit is set or not at Nth position
