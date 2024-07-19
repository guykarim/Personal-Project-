'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        self._max_gain(root)
        return self.max_sum

    def _max_gain(self, node):
        if not node:
            return 0

        # Recursively get the maximum gain from the left and right subtrees
        left_gain = max(self._max_gain(node.left), 0)
        right_gain = max(self._max_gain(node.right), 0)

        # Current path sum including the current node
        current_path_sum = node.val + left_gain + right_gain

        # Update the global maximum path sum
        self.max_sum = max(self.max_sum, current_path_sum)

        # Return the maximum gain that can be extended to the parent node
        return node.val + max(left_gain, right_gain)
