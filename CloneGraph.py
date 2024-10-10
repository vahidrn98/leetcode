"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        nodes = {}
        
        newNode = self.clone(node,nodes)

        return newNode
    

    def clone(self,node,nodes):
        newNode = Node(node.val,None)
        nodes[node] = newNode
        newNeighbors = []

        for neighbor in node.neighbors:
            if(neighbor in nodes):
                newNeighbor = nodes[neighbor]
            else:
                newNeighbor = self.clone(neighbor,nodes)
            newNeighbors.append(newNeighbor)
        
        newNode.neighbors = newNeighbors

        return newNode

        