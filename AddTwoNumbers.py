# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = l1
        r = 0
        mul = 1
        while(head1):
            r+=head1.val * mul
            mul *=10
            head1 = head1.next
        
        head2 = l2
        r2 =0 
        mul = 1
        while(head2):
            r2+=head2.val*mul
            mul*=10
            head2 = head2.next
        
        s = r+r2
        remain = s%10
        ll = ListNode(remain)
        new_head = ll
        s = s //10

        while(s!=0):
            remain = s%10
            n = ListNode(remain)
            ll.next = n
            ll = ll.next
            s = s//10
        
        return new_head
        