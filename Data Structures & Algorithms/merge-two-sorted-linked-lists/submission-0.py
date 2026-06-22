# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        seq1, seq2 = list1, list2
        dummy = ListNode()
        new = dummy
        while seq1 and seq2:
            if seq1.val <= seq2.val:
                new.next = seq1
                seq1 = seq1.next
            else:
                new.next = seq2
                seq2 = seq2.next
            new = new.next
        if seq1:
            new.next = seq1
        elif seq2:
            new.next = seq2
        return dummy.next


            

