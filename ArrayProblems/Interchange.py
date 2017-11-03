def interchange(array,k):
    low,high,n = 0, len(array)-1,len(array)
    x = min(k,n-k)
    for i in range(x):
        array[low],array[high] = array[high],array[low]
        low +=1
        high -= 1



def rotateArray(array,k):

    for i in range(k):
        temp = array[0]

        for j in range(len(array)-1):
            array[j]=array[j+1]
        array[j+1] = temp


# Round robin tournamnet scheduling:


def leftRotate(array):
    temp = array[1]
    length = len(array)
    for i in range(1, length-1):
        array[i] = array[i + 1]

    array[length - 1] = temp


def insertPairing(array):

    n = len(array) // 2
    for i in range(n):
        print(str(array[i])+"  "+str(array[i+n]))
    pass


def getTimeTable(array):
    for i in range(len(array)-1):
        insertPairing(array)
        leftRotate(array)
        print("--------------")


x = [1, 2, 3, 4, 5, 6]
getTimeTable(x)


