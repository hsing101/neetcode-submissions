# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        curr = None
        while last:
            pres = last.next
            last.next = curr
            curr = last
            last = pres
        return curr



        
        