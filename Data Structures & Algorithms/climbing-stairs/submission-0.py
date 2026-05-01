class Solution:
    def climbStairs(self, n: int) -> int:

        # it's fibonacci starting from 1
        if n == 1:
            return 1
        
        res = 1
        prev = 1
        pprev = 0

        for i in range(n):
            res = prev + pprev
            pprev = prev
            prev = res

        return res



        