class Solution:

    def totalHourSpend(self, piles, k):
        total_hour = 0
        for i in range(len(piles)):
            total_hour += (piles[i]//k + (piles[i] % k != 0))
        return total_hour
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        k = max(piles)
        l = 1 # slowest
        r = k # fastest


        # range search
        while l <= r:
            m = l + (r - l) // 2 # google overflow protection

            # since we're looking for any possibility that's smaller but largest withing h hour
            if self.totalHourSpend(piles, m) <= h: # within or eaqual to h continue to probe toward slower
                r = m - 1
            elif self.totalHourSpend(piles, m) > h: # slower than h hour need to probe toward faster
                l = m + 1
        # now r < l there are 2 scenarios
        # r and l was the lower bound before r does m - 1. so only l represents the solution
        # r wasn't fast enough so l is correct one (l = m + 1)
        return l
        






        

        

        