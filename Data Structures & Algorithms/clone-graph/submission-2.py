"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node.val in oldToNew:
                return oldToNew[node.val]
            else:
                copy = Node(node.val)
                oldToNew[node.val] = copy
                for neighbor in node.neighbors:
                    copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node is not None else None