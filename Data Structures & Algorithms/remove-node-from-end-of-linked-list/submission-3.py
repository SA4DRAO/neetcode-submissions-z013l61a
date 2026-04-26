# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        


        # Removing nth node = Removing (len(list)-n)th node
        cntr = 0
        s = head
        while s is not None:
            cntr += 1
            s = s.next
        
        cntr = cntr - n

        if cntr == 0:
            return head.next
        


        r = head
        for i in range(cntr-1):
            r = r.next
        
        r.next = r.next.next
        
        return head