class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        mins = 0
        q = deque()
        rotten = set()
        fresh = set()


        # search of the c, r for rotten fruit
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))

        
        while q:
            if len(fresh) == 0:
                print(mins)
                return mins
            for i in range(len(q)):
                r, c = q.popleft()
                print(grid)
                print(mins)
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for nr, nc in neighbors:
                    if min(r + nr, c + nc) < 0 or r + nr == ROWS or c + nc == COLS or grid[r + nr][c + nc] == 0 or (r + nr, c + nc) in rotten :
                        continue
                    grid[r + nr][c + nc] = 2
                    q.append((r + nr, c + nc))
                    rotten.add((r + nr, c + nc))
                    fresh.remove((r + nr, c + nc))
            mins += 1
        
        if len(rotten) == 0 and len(fresh) == 0:
            return 0
        return - 1
        

            


        






        