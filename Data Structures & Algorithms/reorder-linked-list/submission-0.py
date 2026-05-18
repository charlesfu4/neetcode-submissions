# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # split the link list into 2 portions
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # now reverse the second half link list for correct sequence

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        

        # and then we need to tick the pointer starting from each end inward

        l, r = head, prev
        # always make sure there is r node
        while r:
            tmp1, tmp2 = l.next, r.next
            l.next = r
            r.next = tmp1
            l, r = tmp1, tmp2
    




