# no of set bits in log n time.

def getCountBit(n):
    count = 0
    while n>0:
       n = n & n-1
       print("n is ",n)
       count +=1
    return count

print(getCountBit(15))