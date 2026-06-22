# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        point1 = list1
        point2 = list2
        head = ListNode(None)
        curr = head
        while point1 and point2:
            if point1.val >= point2.val:
                curr.next = point2
                curr = curr.next
                point2 = point2.next
            else:
                curr.next = point1
                curr = curr.next
                point1 = point1.next
        if point1:
            curr.next = point1
        elif point2:
            curr.next = point2
        return head.next


            


