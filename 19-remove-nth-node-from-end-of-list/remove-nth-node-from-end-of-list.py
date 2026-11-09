# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cur = head
        count = 0
        originalHead = head
        for i in range(0,n):
            cur = cur.next
        if cur is None:
            return head.next
        while cur:
            if count != 0 :
                head = head.next
            count+=1
            cur = cur.next
        head.next = head.next.next
        return originalHead
