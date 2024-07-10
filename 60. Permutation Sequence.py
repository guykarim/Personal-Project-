'''The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        
        # Create a list of numbers to get elements from
        numbers = list(range(1, n + 1))
        
        # Convert k to zero-based index
        k -= 1
        
        # Initialize result
        result = []
        
        # Calculate factorial of (n - 1)
        factorial = math.factorial(n - 1)
        
        # Build the k-th permutation
        for i in range(n - 1, -1, -1):
            index = k // factorial
            result.append(str(numbers[index]))
            numbers.pop(index)
            
            if i != 0:
                k %= factorial
                factorial //= i
        
        return ''.join(result)
