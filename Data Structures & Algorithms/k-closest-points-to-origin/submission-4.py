class Solution:

    def disToOrigin(self, point: List[int]) -> int:
        return point[0] * point[0] + point[1] * point[1]

    def mergeSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        m = (e + s)//2

        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)

        self.merge(arr, s, m, e)

        return arr
    
    def merge(self, arr, s, m, e):

        larr = arr[s : m + 1]
        rarr = arr[m + 1 : e + 1]

        i = 0 
        j = 0
        k = s

        while  i < len(larr) and j < len(rarr):
            if self.disToOrigin(larr[i]) <= self.disToOrigin(rarr[j]):
                arr[k] = larr[i]
                i += 1
            else:
                arr[k] = rarr[j]
                j += 1
            k += 1
        while i < len(larr):
            arr[k] = larr[i]
            i += 1
            k += 1
        while j < len(rarr):
            arr[k] = rarr[j]
            j += 1
            k += 1


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        s = 0
        e = len(points)

        sortedPoints = self.mergeSort(points, s, e)

        print(sortedPoints)

        return sortedPoints[0: k]
        








        