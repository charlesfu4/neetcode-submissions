
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        q = deque([node])
        visited = {}
        visited[node] = Node(node.val)



        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]
