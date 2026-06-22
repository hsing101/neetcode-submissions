# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        if root:
            que.append(root)
        result = []
        while que:
            l = len(que)
            level = []
            for i in range(l):
                curr = que.popleft()
                if curr:
                    level.append(curr.val)
                    que.append(curr.left)
                    que.append(curr.right)
            if level:
                result.append(level)
        return result


        