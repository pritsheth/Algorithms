# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# USe Python 2.7 : Queue
from queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        pq = PriorityQueue()
        temp = ListNode(0)
        head = temp

        for node in lists:
            if node:
                pq.put((node.val, node.next))

        while not pq.empty():
            smallest_node = pq.get()
            print(smallest_node)
            temp.next = ListNode(smallest_node[0])
            temp = temp.next
            if smallest_node[1] is not None:
                pq.put((smallest_node[1].val, smallest_node[1].next))

        return head.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l1.next = l2
l2.next = l3

s = Solution()
s.mergeKLists([l1,l2])
