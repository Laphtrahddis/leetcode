# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # p1=head.next
        # p2=head.next.next
        # while p2 and p2.next:
        #     p1.val,p2.val=p2.val,p1.val
        #     p1=p1.next
        #     p2=p2.next.next
        # p1.val,p2.val=p2.val,p1.val
        # return head
        if not head or not head.next:
            return head
        even,odd=head.next,head
        evenhead=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenhead
        return head
