# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        _,main_head = self.count(None,head,head,n)

        return main_head


    def count(self,prev,head,main_head,n):
        if(head is None):
            return 0,main_head
        c , main_head = self.count(head,head.next,main_head,n)
        c +=1
        if(c==n):
            if(prev):
                prev.next = head.next
            else:
                main_head = head.next

        return c, main_head
        