# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if not odd:
            return head
        even = head.next
        orig_even = even

        orig_head = head

        if even:
            head = even.next
        else:
            odd.next = even
            return odd

        i = 1
        while(head):
            if(i==1):
                odd.next = head
                odd = odd.next
                i=0
            else:
                even.next = head
                even = even.next
                i=1
            head = head.next

        even.next = None
        odd.next = orig_even
       

        return orig_head
        