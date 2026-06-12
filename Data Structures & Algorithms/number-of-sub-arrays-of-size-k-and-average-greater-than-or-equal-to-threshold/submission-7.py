class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        st = k * threshold
        L, R  = 0, 0
        total = arr[L]

        while R < len(arr) - 1:
            if total >= st and R - L + 1 == k:
                counter += 1
            
            print(total)

            R += 1
            # check if the window is larger than k 
            # if so remove the L and tip it forward
            if R - L + 1 > k:
                total -= arr[L]
                L += 1
            total += arr[R]
        
        if total >= st:
            counter += 1

        
        return counter




