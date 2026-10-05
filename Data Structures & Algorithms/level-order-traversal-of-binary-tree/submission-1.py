# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        def dfs(root, depth):
            if root is None:
                return
            levels[depth].append(root.val)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        
        res = []
        for i in range(len(levels)):
            res.append(levels[i])

        return res