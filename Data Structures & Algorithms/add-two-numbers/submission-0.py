# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = n2 = 0
        d1 = d2 = -1
        while l1:
            d1 += 1
            n1 += l1.val*10**d1
            l1 = l1.next
        
        while l2:
            d2 += 1
            n2 += l2.val*10**d2
            l2 = l2.next
        
        res = str(n1 + n2)
        print(res)

        start = node = ListNode()

        for i in range(len(res) - 1, -1, - 1):
            node.val = int(res[i])
            if i != 0:
                node.next = ListNode()
                node = node.next
            else:
                node.next = None
        
        return start









        

        return l1

        