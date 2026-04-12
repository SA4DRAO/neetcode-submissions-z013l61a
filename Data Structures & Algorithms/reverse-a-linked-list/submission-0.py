# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head


        prev = None
        curr = head
        new = head.next
        while True:
            if curr is None:
                
                break

            curr.next = prev
            prev = curr
            curr = new
            if new is None:
                return prev
            new = new.next
        return prev