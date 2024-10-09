# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if(not root):
            return []

        q = deque()
        q.append(root)
        right = []

        while(q):
            level = deque()

            first = q[-1]
            right.append(first.val)

            while(q):
                node = q.popleft()
                if(node.left):
                    level.append(node.left)
                if(node.right):
                    level.append(node.right)

            while(level):
                q.append(level.popleft())

        return right


        

        
        