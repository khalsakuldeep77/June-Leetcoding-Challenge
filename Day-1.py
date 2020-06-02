
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        #this is the recursive function which will reach the leaf node first and then start swapping
        def helper(node):
            if node==None:
                return 
            else:
                temp=node
                helper(node.left)
                helper(node.right)
                temp=node.left
                node.left=node.right
                node.right=temp
        
        helper(root)
        
        return root