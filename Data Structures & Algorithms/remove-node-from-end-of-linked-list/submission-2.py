# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr1 = head
        curr2 = head
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        for i in range(n):
            curr2 = curr2.next            
        
        while curr2:
            prev = curr1
            curr1 = curr1.next
            curr2 = curr2.next

        
        prev.next = curr1.next
        return dummy.next
        