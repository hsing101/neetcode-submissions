# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None

        root = preorder[0]
        node = TreeNode(root)
        j = inorder.index(root)

        leftpart = inorder[0 : j]
        rightpart = inorder[j + 1 : ]

        leftp = preorder[1 : len(leftpart) + 1]
        rightp = preorder[len(leftpart) + 1 :]

        
        node.left = self.buildTree(leftp, leftpart)
        node.right = self.buildTree(rightp, rightpart)
        
        return node
        
        


        