class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])

        visited = set()
        originalColor = image[sr][sc]

        def dfs(image, sr, sc, visited):

            # base cases
            if min(sr, sc) < 0 or sr == ROWS or sc == COLS or (sr, sc) in visited or image[sr][sc] != originalColor:
                return
            else:
                visited.add((sr, sc))
                image[sr][sc] = color
            
    
            dfs(image, sr + 1, sc, visited)
            dfs(image, sr - 1, sc, visited)
            dfs(image, sr, sc + 1, visited)
            dfs(image, sr, sc - 1, visited)
        
        dfs(image, sr, sc, visited)


        return image
