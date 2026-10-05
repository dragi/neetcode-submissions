class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeToNeighbors = {i:[] for i in range(n)}
        visited = set()

        for node, neighbor in edges:
            nodeToNeighbors[node].append(neighbor)
            nodeToNeighbors[neighbor].append(node)

        def dfs(node, visited, prev):
            if node in visited:
                return False
            visited.add(node)
            
            for nei in nodeToNeighbors[node]:
                if nei != prev:
                    if not dfs(nei, visited, node):
                        return False
            return True

        return dfs(0, visited, None) and len(visited) == n