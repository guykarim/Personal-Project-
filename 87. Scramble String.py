'''
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):  # If they have different characters
            return False
        
        n = len(s1)
        dp = [[[False] * (n+1) for _ in range(n)] for __ in range(n)]

        # Initialization
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = (s1[i] == s2[j])
        
        # dp[i][j][k] means whether s1[i:i+k] is a scramble of s2[j:j+k]
        for k in range(2, n+1):  # Substring lengths from 2 to n
            for i in range(n-k+1):  # Starting index of the substring in s1
                for j in range(n-k+1):  # Starting index of the substring in s2
                    for q in range(1, k):  # Split the substring into two parts
                        if (dp[i][j][q] and dp[i+q][j+q][k-q]) or (dp[i][j+k-q][q] and dp[i+q][j][k-q]):
                            dp[i][j][k] = True
                            break
        
        return dp[0][0][n]

# Example usage
solution = Solution()
print(solution.isScramble("great", "rgeat"))  # Output: True
print(solution.isScramble("abcde", "caebd"))  # Output: False
print(solution.isScramble("a", "a"))          # Output: True
