
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

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

    def printList(self, head):

        while head != None:
            print(head.val)
            head = head.next

    def getMiddleNode(self, head):

        slow = head
        fast = head

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        print("middle is ", slow.val)
        return slow

        # def sortList(self, head):

    def partition(self, head, x):

        temp = head
        pre = head
        result = ListNode(0)
        answer = result

        if head is None:
            return None

        while (temp != None):
            if temp.val > x:
                # print(temp.val)
                pre.next = temp.next  # Deleting the node
                result.next = temp
                result = result.next
                temp = temp.next
                continue

            pre = temp
            temp = temp.next

        # self.printList(pre)
        pre.next = answer.next
        return head



l1 = ListNode(1)
l2 = ListNode(6)
l3 = ListNode(2)
l4 = ListNode(5)
l5 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

list = [1,2,3,4]
print("cond",list)

s = Solution()
s.partition(l1, 3)
# s.removeNthFromEnd(l1, 2)
