# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # if root.left:
        #     self.invertTree(root.left)
        # if root.right:
        #     self.invertTree(root.right)
        # if root.left and root.right:
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root





        # while curr.left or curr.right:
        #     if curr.left and curr.right:
        #         temp = curr.left
        #         curr.left = curr.right
        #         curr.right = temp
        #     curr = curr.
            