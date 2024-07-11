'''
There is a family tree rooted at 0 consisting of n nodes numbered 0 to n - 1. You are given a 0-indexed integer array parents, where parents[i] is the parent for node i. Since node 0 is the root, parents[0] == -1.

There are 105 genetic values, each represented by an integer in the inclusive range [1, 105]. You are given a 0-indexed integer array nums, where nums[i] is a distinct genetic value for node i.

Return an array ans of length n where ans[i] is the smallest genetic value that is missing from the subtree rooted at node i.

The subtree rooted at a node x contains node x and all of its descendant nodes.

 

Example 1:


Input: parents = [-1,0,0,2], nums = [1,2,3,4]
Output: [5,1,1,1]
Explanation: The answer for each subtree is calculated as follows:
- 0: The subtree contains nodes [0,1,2,3] with values [1,2,3,4]. 5 is the smallest missing value.
- 1: The subtree contains only node 1 with value 2. 1 is the smallest missing value.
- 2: The subtree contains nodes [2,3] with values [3,4]. 1 is the smallest missing value.
- 3: The subtree contains only node 3 with value 4. 1 is the smallest missing value.
Example 2:


Input: parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]
Output: [7,1,1,4,2,1]
Explanation: The answer for each subtree is calculated as follows:
- 0: The subtree contains nodes [0,1,2,3,4,5] with values [5,4,6,2,1,3]. 7 is the smallest missing value.
- 1: The subtree contains nodes [1,2] with values [4,6]. 1 is the smallest missing value.
- 2: The subtree contains only node 2 with value 6. 1 is the smallest missing value.
- 3: The subtree contains nodes [3,4,5] with values [2,1,3]. 4 is the smallest missing value.
- 4: The subtree contains only node 4 with value 1. 2 is the smallest missing value.
- 5: The subtree contains only node 5 with value 3. 1 is the smallest missing value.
Example 3:

Input: parents = [-1,2,3,0,2,4,1], nums = [2,3,4,5,6,7,8]
Output: [1,1,1,1,1,1,1]
Explanation: The value 1 is missing from all the subtrees.
 

Constraints:

n == parents.length == nums.length
2 <= n <= 105
0 <= parents[i] <= n - 1 for i != 0
parents[0] == -1
parents represents a valid tree.
1 <= nums[i] <= 105
Each nums[i] is distinct.
'''
class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        from collections import defaultdict

        n = len(parents)
        tree = defaultdict(list)

        # Create the tree representation
        for i in range(1, n):
            tree[parents[i]].append(i)

        # Initialize the result array with 1s
        ans = [1] * n

        # Find the index of the node with genetic value 1
        one_index = -1
        for i in range(n):
            if nums[i] == 1:
                one_index = i
                break

        if one_index == -1:
            # If there's no genetic value 1, all answers are 1
            return ans

        # Helper function to perform DFS and find all genetic values in a subtree
        def dfs(node, seen, current_missing):
            stack = [node]
            while stack:
                u = stack.pop()
                if not seen[nums[u]]:
                    seen[nums[u]] = True
                    for v in tree[u]:
                        stack.append(v)
            # Find the smallest missing value
            while seen[current_missing]:
                current_missing += 1
            return current_missing

        # Initialize the seen array and current_missing value
        seen = [False] * (10**5 + 2)  # To handle values from 1 to 10^5
        current_missing = 1

        # Start from the node with genetic value 1 and move up to the root
        current = one_index
        while current != -1:
            current_missing = dfs(current, seen, current_missing)
            ans[current] = current_missing
            current = parents[current]

        return ans

# Example usage:
parents = [-1, 0, 0, 2]
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.smallestMissingValueSubtree(parents, nums))  # Output: [5, 1, 1, 1]

parents = [-1, 0, 1, 0, 3, 3]
nums = [5, 4, 6, 2, 1, 3]
print(solution.smallestMissingValueSubtree(parents, nums))  # Output: [7, 1, 1, 4, 2, 1]

parents = [-1, 2, 3, 0, 2, 4, 1]
nums = [2, 3, 4, 5, 6, 7, 8]
print(solution.smallestMissingValueSubtree(parents, nums))  # Output: [1, 1, 1, 1, 1, 1, 1]
