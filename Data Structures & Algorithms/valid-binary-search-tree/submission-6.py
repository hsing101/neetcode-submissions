# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        if not root:
            return True

        leftNode = root.left
        rightNode = root.right


        if not leftNode and not rightNode:
            return True

        if leftNode:
            leftVal = leftNode.val
            while leftNode.right:
                leftNode = leftNode.right
                leftVal = leftNode.val
        else:
            leftVal = root.val - 1
        
        if rightNode:
            rightVal = rightNode.val
            while rightNode.left:
                rightNode = rightNode.left
                rightVal = rightNode.val
        else:
            rightVal = root.val + 1

        if root.val > leftVal and root.val < rightVal:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
