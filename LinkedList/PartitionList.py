# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        n1 = low = ListNode(0)
        n2 = high = ListNode(0)

        while head is not None:
            if head.val < x:
                n1.next = head
                n1 = n1.next
            else:
                n2.next = head
                n2 = n2.next
            head = head.next

        n1.next = high.next
        n2.next = None
        return low.next
