'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        
        l, r = 0, 0
        formed = 0
        
        window_counts = defaultdict(int)
        min_length = float('inf')
        min_left, min_right = 0, 0
        
        while r < len(s):
            character = s[r]
            window_counts[character] += 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_left, min_right = l, r
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if min_length == float('inf') else s[min_left:min_right + 1]

# Example usage:
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(sol.minWindow("a", "a"))  # Output: "a"
print(sol.minWindow("a", "aa"))  # Output: ""
