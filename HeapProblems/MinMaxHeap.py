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


    def add_withPriorityNumber(self,pq):
        heapq.heappush(pq, (1,"hi"))
        heapq.heappush(pq, (10,"hi"))
        heapq.heappush(pq, (2,"hi"))

        x = heapq.heappop(pq)
        print("popped: ", x)


    def getLargest(self, list):
        pass


hp = HeapQueueProblems()
hp.get_smallest([34, 2, 1])
hp.add_withPriorityNumber([])
