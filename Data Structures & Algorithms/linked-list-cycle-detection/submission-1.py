# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tort, hare = head, head
        while hare and hare.next:
            tort, hare = tort.next, hare.next.next
            if hare == tort:
                return True
        return False
        