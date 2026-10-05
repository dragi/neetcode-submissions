class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeToNeighbors = {i:[] for i in range(n)}
        visited = set()

        for n1, n2 in edges:
            nodeToNeighbors[n1].append(n2)
            nodeToNeighbors[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for nei in nodeToNeighbors[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n