# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None or root.val > subRoot.val:
            return False
        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)