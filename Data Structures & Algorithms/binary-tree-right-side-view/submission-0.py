# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def levelOrder(root):
            if not root:
                return [[]]
            queue = deque()
            queue.append(root)
            ans = [[root.val]]
            while queue:
                layer = []
                length = len(queue)
                for i in range(length):
                    node = queue.popleft()
                    if node.left:
                        layer.append(node.left.val)
                        queue.append(node.left)
                    if node.right:
                        layer.append(node.right.val)
                        queue.append(node.right)
                if len(layer) > 0:
                    ans.append(layer)
            return ans
        layers = levelOrder(root)
        for layer in layers:
            if len(layer) > 0:
                ans.append(layer[-1])
        return ans

                    
                


        