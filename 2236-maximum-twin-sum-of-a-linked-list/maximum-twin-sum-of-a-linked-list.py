# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow,fast=head,head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            tmp=slow.next
            slow.next=prev 
            prev=slow            
            slow=tmp
        res=0
        while slow and prev:
            res=max(res,slow.val+prev.val)
            slow=slow.next
            prev=prev.next
        return res
            