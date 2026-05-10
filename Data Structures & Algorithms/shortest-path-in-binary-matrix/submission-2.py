class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        queue = deque()
        
        if grid[0][0] != 1:
            visited.add((0,0))
            queue.append((0,0))
        else:
            return -1
    
        length = 1

        while queue:
            for i in range(len(queue)):
                cr, cc = queue.popleft()
                if cr == ROWS - 1 and cc == COLS - 1:
                    if grid[cr][cc] == 0:
                        return length
                
                neighbors = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [-1, 1], [1, -1]]
    
                for ar, ac in neighbors:
                    if min(cr + ar, cc + ac) < 0 or (cr + ar, cc + ac) in visited or cr + ar == ROWS or cc + ac == COLS or grid[cr + ar][cc + ac] == 1:
                        continue
                    queue.append((cr + ar, cc + ac))
                    visited.add((cr + ar, cc + ac))
            length += 1
        
        return -1

                
        