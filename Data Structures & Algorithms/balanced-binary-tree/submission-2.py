from typing import Optional, Tuple

class Solution:
    def isBalanced(self, root: Optional['TreeNode']) -> bool:
        def dfs(node: Optional['TreeNode']) -> Tuple[bool, int]:
            if not node:
                return True, 0  # (is_balanced, depth)

            left_bal, left_depth = dfs(node.left)
            right_bal, right_depth = dfs(node.right)

            balanced = left_bal and right_bal and abs(left_depth - right_depth) <= 1
            depth = 1 + max(left_depth, right_depth)

            return balanced, depth

        return dfs(root)[0]