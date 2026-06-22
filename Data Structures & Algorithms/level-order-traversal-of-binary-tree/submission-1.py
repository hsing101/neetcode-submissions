# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        if not root:
            return []
        que.append(root)
        soln = [[root.val]]
        while que:
            size = len(que)
            row = []
            for i in range(size):
                pop = que.popleft()
                if pop.left:
                    que.append(pop.left)
                if pop.right:
                    que.append(pop.right)
            for num in que:
                row.append(num.val)
            if len(row) > 0:
                soln.append(row)
        return soln
            