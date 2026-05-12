class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = 0

        while l < r:
            area = min(heights[r], heights[l]) * (r - l)
            max_area = max(area, max_area)

            # search inward to seek higher bar on the short bar side
            # and keep the long bar
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

            

        


            
        