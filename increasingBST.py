# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        def helper(root):
            if root is None:
                return 
            helper(root.left)
            l.append(root.val)
            helper(root.right)
        helper(root)
        Node=val=TreeNode(-1)
        for v in l:
            val.right=TreeNode(v)
            val=val.right 
        return Node.right
            
            
        