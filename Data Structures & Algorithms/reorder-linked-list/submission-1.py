# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse second half of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # if fast == None: # slow is at halfway. ODD list
        #     pass
        # else: # fast.next == None. slow is just before halfway. EVEN list
        #     pass

        #REVERSE LINKED LIST
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        start, front_prev, front, back = head, head, head.next, prev

        # front = head
        # while front.next and front != back:
        while back:
            temp = back.next
            front = front_prev.next
            front_prev.next = back
            # front.next = back.next
            back.next = front

            front_prev, back = front, temp
