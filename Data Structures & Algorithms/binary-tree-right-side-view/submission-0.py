# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        res = []
        
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            tmp = []
            counter = 0
            for i in range(len(q)):
                curr = q.popleft()
                tmp.append(curr.val)
                counter += 1
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(tmp[counter - 1])
            
        return res
                
            
                

        
        