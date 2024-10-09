# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        self.inOrder(root,stack)
        for i in range(len(stack)-1):
            if(stack[i]>=stack[i+1]):
                return False
        return True
    
    def inOrder(self,root,stack):
        if(not root):
            return

        self.inOrder(root.left,stack)
        stack.append(root.val)
        self.inOrder(root.right,stack)

            

        