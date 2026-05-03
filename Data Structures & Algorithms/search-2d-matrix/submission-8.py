class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        m = len(matrix[0])
        n = len(matrix)
        r = m*n - 1
        print(m)
        print(n)

        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid//m][mid%m]:
                r = mid - 1
            elif target > matrix[mid//m][mid%m]:
                l = mid + 1
            else:
                return True
        return False



        