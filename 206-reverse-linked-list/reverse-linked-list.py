# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head):
            if not head or not head.next:
                return head
            newhead=reverse(head.next)
            front=head.next
            front.next=head
            head.next=None
            return newhead
        newhead=reverse(head)
        return newhead
        
            
