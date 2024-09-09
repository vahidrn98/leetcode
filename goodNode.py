# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return 1+ self.find(root.left,root.val) + self.find(root.right,root.val)
    
    def find(self,root,x):

        if not root:
            return 0

        if(root.val>=x):
            return 1+ self.find(root.left,root.val) + self.find(root.right,root.val)
        else:
            return self.find(root.left,x) + self.find(root.right,x)
        