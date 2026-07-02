# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees are identical.
        Two trees are identical if they have the same structure and node values.

        Args:
            p: Root node of the first binary tree
            q: Root node of the second binary tree

        Returns:
            True if both trees are identical, False otherwise
        """

        if p is None and q is None:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same
