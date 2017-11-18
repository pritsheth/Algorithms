class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):

        temp = head
        fast = head

        if head.next == None and n >= 1:
            return []

        while fast.next != None and n > 1:
            fast = fast.next
            n -= 1

        pre = head
        while fast.next != None:
            pre = temp
            temp = temp.next
            fast = fast.next

        if pre != temp:
            pre.next = pre.next.next
        else:
            head = head.next
        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4

s = Solution()
s.removeNthFromEnd(l1, 2)
