"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        for node in node_map.keys():
            node_map[node].next = node_map.get(node.next)
            node_map[node].random = node_map.get(node.random)
        return node_map.get(head)




         
        