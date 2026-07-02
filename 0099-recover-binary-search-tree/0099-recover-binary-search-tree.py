# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def inorder_traversal(node: Optional[TreeNode]) -> None:

            if node is None:
                return
          
            nonlocal previous_node, first_swapped, second_swapped

            inorder_traversal(node.left)

            if previous_node and previous_node.val > node.val:
                if first_swapped is None:

                    first_swapped = previous_node

                second_swapped = node

            previous_node = node

            inorder_traversal(node.right)

        previous_node = None     
        first_swapped = None     
        second_swapped = None     

        inorder_traversal(root)

        first_swapped.val, second_swapped.val = second_swapped.val, first_swapped.val