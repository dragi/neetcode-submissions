# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l = min(p.val, q.val)
        r = max(p.val, q.val)

        while not (l <= root.val <= r):
            if root.val > l:
                root = root.left
            else:
                root = root.right
        return root