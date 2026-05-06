class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            base = arr[i]  
            rmax = 0
            for j in range(i+1, len(arr)):
                if arr[j] > rmax:
                    rmax = arr[j]
            arr[i] = rmax
        arr[len(arr)-1] = -1
        return arr


