# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the midpoint
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Reverse from the midpoint
        prev, current = None, slow.next
        slow.next = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        

        # Now the lists are
        # current and head

        # Merge the two lists.
        first, second = head,prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2



         