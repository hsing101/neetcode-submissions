# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        root = preorder[0]
        node = TreeNode(root)
        j = inorder.index(root)

        leftpart = inorder[0 : j]
        rightpart = inorder[j + 1 : ]

        leftp = preorder[1 : len(leftpart) + 1]
        rightp = preorder[len(leftpart) + 1 :]

        if len(leftpart) == 0:
            node.left = None
        elif len(leftpart) == 1:
            node.left = TreeNode(leftpart[0])
        else:
            node.left = self.buildTree(leftp, leftpart)

        if len(rightpart) == 0:
            node.right = None
        elif len(rightpart) == 1:
            node.right = TreeNode(rightpart[0])
        else:
            node.right = self.buildTree(rightp, rightpart)
        
        return node
        
        


        