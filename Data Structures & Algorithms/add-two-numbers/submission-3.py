# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        carry = 0
        while l1 and l2:
            dig = l1.val + l2.val + 1 if carry == 1 else l1.val + l2.val
            if dig > 9:
                dig %= 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(dig)
            l1 = l1.next
            l2 = l2.next
            res = res.next
        
        while l1:
            dig = l1.val + 1 if carry == 1 else l1.val
            if dig > 9:
                dig %= 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(dig)
            res = res.next
            l1 = l1.next
        
        while l2:
            dig = l2.val + 1 if carry == 1 else l2.val
            if dig > 9:
                dig %= 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(dig)
            res = res.next
            l2 = l2.next

        if carry == 1:
            res.next = ListNode(1)

        return dummy.next
        

            
            
            