# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        hmap = defaultdict(int)

        if head:
            while head.next:
                if hmap[head.val] == 0:
                    hmap[head.val] += 1
                    head = head.next
                else:
                    return True
        
        return False

            
        

        