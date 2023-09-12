# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val > q.val and root.val < p.val) or (root.val < q.val and root.val > p.val):
            return root
        elif (root.val > q.val and root.val == p.val) or (root.val > p.val and root.val == q.val):
            return root
        elif (root.val < q.val and root.val == p.val) or (root.val < p.val and root.val == q.val):
            return root
        elif (q.val < root.val) and (p.val < root.val):
            root = root.left
            return self.lowestCommonAncestor(root, p, q)
        elif (q.val > root.val) and (p.val > root.val):
            root = root.right
            return self.lowestCommonAncestor(root, p, q)
        else:
            return None
            