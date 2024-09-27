# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        q = deque()
        q.append(root)
        level = []
        ans = [[root.val]]
        while(len(q)>0):
            temp = deque()

            while(len(q)>0):
                node = q.popleft()
                if(node.left):
                    temp.append(node.left)
                if(node.right):
                    temp.append(node.right)

            a = []
            while(len(temp)>0):
                node = temp.popleft()
                a.append(node.val)
                q.append(node)
                
            if(len(a)>0):
                ans.append(a)
        
        return ans

        