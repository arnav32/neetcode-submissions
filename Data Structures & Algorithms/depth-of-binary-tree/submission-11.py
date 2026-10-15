# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s = [(root, 1)]
        depth = 0
        while s:
            popped, cur_depth = s.pop()
            depth = max(depth, cur_depth)
            if popped.left:
                s.append((popped.left, cur_depth + 1))
            if popped.right:
                s.append((popped.right, cur_depth + 1))
        return depth