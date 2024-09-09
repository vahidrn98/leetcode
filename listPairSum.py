# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        sums = []
        i=0
        orig_head = head
        n=0

        while(head):
            n+=1
            head = head.next

        head = orig_head
        while(head):

            if(i+1<=n//2):
                
                stack.append(head.val)
            else:
                # print(i+1)
                sums.append(stack.pop()+head.val)

            head = head.next
            i+=1

        return max(sums)