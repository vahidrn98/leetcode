# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n=0
        orig_head = head
        while(head):
            n+=1
            head = head.next

        i=0
        head = orig_head
        prev = ListNode(-1,orig_head)

        if(not orig_head.next):
            return 
        
        while(head):
            a = head.val
            if i==n//2:
                prev.next = head.next
            
            prev = head
            head = head.next

            i+=1
            
        return orig_head
        