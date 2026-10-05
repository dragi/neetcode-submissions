class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        nodeToNeighbors = {i:[] for i in range(n)}
        for n1, n2 in edges:
            nodeToNeighbors[n1].append(n2)
            nodeToNeighbors[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)

            for nei in nodeToNeighbors[node]:
                if nei != prev:
                    dfs(nei, node)

        count = 0
        for i in range(n):
            if len(nodeToNeighbors[i]) > 0:
                if nodeToNeighbors[i][0] not in visited:
                    count += 1
                dfs(i, -1)
            else:
                count += 1

        return count