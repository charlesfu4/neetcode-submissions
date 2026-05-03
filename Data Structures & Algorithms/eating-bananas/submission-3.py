class Solution:

    def totalHourSpend(self, piles, k):
        total_hour = 0
        for i in range(len(piles)):
            total_hour += (piles[i]//k + (piles[i] % k != 0))
        return total_hour
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        k = max(piles)
        l = 1
        r = k


        while l <= r:
            m = (l + r) // 2

            if self.totalHourSpend(piles, m) <= h:
                r = m - 1
            elif self.totalHourSpend(piles, m) > h:
                l = m + 1
        return l
        






        

        

        