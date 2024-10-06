"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        nmap = {}
        if(not head):
            return None
        new_head = Node(head.val)
        nmap[head] = new_head
        head_copy = new_head
        while(head!=None):
            if(head.next!=None):
                if(head.next in nmap):
                    next = nmap[head.next]
                    new_head.next = next
                else:
                    next = Node(head.next.val)
                    nmap[head.next] = next
                    new_head.next = next
            else:
                new_head.next = None
            
            if(head.random!=None):
                if(head.random in nmap):
                    random = nmap[head.random]
                    new_head.random = random
                else:
                    random = Node(head.random.val)
                    nmap[head.random] = random
                    new_head.random = random
            else:
                new_head.random = None
            
            head = head.next
            new_head = new_head.next

        return head_copy
        