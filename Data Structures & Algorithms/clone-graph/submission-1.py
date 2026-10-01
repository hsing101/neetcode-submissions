"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapp = defaultdict(Node)

        def dfs(node):
            if not node:
                return 
            copy = Node(node.val)
            mapp[node] = copy
            for nei in node.neighbors:
                if nei not in mapp:
                    copy.neighbors.append(dfs(nei))
                else:
                    copy.neighbors.append(mapp[nei])
            return copy
        return dfs(node)
        


