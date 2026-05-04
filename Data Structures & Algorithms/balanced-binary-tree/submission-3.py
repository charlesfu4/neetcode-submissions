from typing import Optional, Tuple

class Solution:
    def isBalanced(self, root: Optional['TreeNode']) -> bool:

        def dfs(root) -> Tuple[bool, int]:
            if not root:
                return True, 0
            
            lb, ld = dfs(root.left)
            rb, rd = dfs(root.right)

            b = lb and rb and abs(ld - rd) <= 1
            d = 1 + max(ld, rd)

            return b, d
        
        return dfs(root)[0]