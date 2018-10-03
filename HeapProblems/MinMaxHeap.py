from queue import PriorityQueue


class PriorityQueueProblems:
    def get_smallest(self, A):
        pq = PriorityQueue(4)
        pq.put((10, 1))
        pq.put((0, 2))
        pq.put((110, 3))
        pq.put((1, 3))

        while not pq.empty():
            print(pq.get())


import heapq


def getMaxDifferenceSubset(nums, k):
    min_pq = nums[:k]
    max_pq = [-x for x in nums[:k]]
    heapq.heapify(min_pq)
    heapq.heapify(max_pq)

    for i in range(k, len(nums)):
        addToMaxHeap(max_pq, nums[i])
        addToMinHeap(min_pq, nums[i])

    print(max_pq)
    print(min_pq)

    print(sum(min_pq) + sum(max_pq))


def addToMinHeap(min_pq, num):
    top = min_pq[0]

    if top >= num:
        return
    else:
        heapq.heapreplace(min_pq, num)


def addToMaxHeap(max_pq, num):
    #  Get actual positive value
    top = -max_pq[0]

    if top <= num:
        return
    else:
        heapq.heapreplace(max_pq, -num)  # insert always negative while pushing


getMaxDifferenceSubset([8, 11, 40, 15, 5], 2)


class HeapQueueProblems:

    # Bedefault it min heap
    def get_smallest(self, list):
        heapq.heapify(list)
        print(list)

        heapq.heappush(list, 0)

        print(list)

        x = heapq.heappop(list)
        print("popped: ", x)

        large = heapq.nlargest(2, list)
        print("largest", large)

        small = heapq.nsmallest(3, list)
        print("smallest", small)

    def add_withPriorityNumber(self, pq):
        heapq.heappush(pq, (1, "hi"))
        heapq.heappush(pq, (10, "hi"))
        heapq.heappush(pq, (2, "hi"))

        x = heapq.heappop(pq)
        print("popped: ", x)

    def getLargest(self, list):
        pass


hp = HeapQueueProblems()
hp.get_smallest([34, 2, 1])
hp.add_withPriorityNumber([])
