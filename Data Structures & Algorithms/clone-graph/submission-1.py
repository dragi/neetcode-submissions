"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        if not node.neighbors:
            return Node(node.val, None)
        
        seen = {}

        def dfs(node, seen):
            copy = Node(node.val)
            seen[node.val] = copy

            for i in range(len(node.neighbors)):            
                if node.neighbors[i].val in seen:
                    copy.neighbors.append(seen[node.neighbors[i].val])
                else:
                    copy.neighbors.append(dfs(node.neighbors[i], seen))
            return copy

        return dfs(node, seen)
