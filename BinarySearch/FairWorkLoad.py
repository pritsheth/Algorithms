# https://community.topcoder.com/stat?c=problem_statement&pm=1901&rd=4650



def getMaxLoad(folders, worker):
    low = max(folders)
    high = sum(folders)
    require_worker = 0
    while low < high:

        mid = (low + high) >> 1

        require_worker = countWorkers(folders, mid)[0]
        if require_worker == worker:
            return mid

        if require_worker < worker:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def countWorkers(folders, maxLoad):
    temp = 0
    require_worker = 0
    maxi = 0
    for i in folders:
        temp += i
        if temp >= maxLoad:
            maxi = max(maxi, temp)
            temp = 0
            require_worker += 1

    return require_worker, maxi


folders = [10, 20, 30, 40, 50, 60, 70, 80, 90]
max_w = getMaxLoad(folders, 3)
print(countWorkers(folders, max_w)[1])
