
--127. Word Ladder
Solved
Hard
Topics
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.--end


from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Convert wordList to a set for efficient lookup
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Initialize BFS queue with the beginWord and level 1
        queue = deque([(beginWord, 1)])

        while queue:
            current_word, level = queue.popleft()

            # Generate all possible transformations of current_word
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # Change one letter at a time
                    next_word = current_word[:i] + char + current_word[i+1:]

                    # Check if the transformed word is the endWord
                    if next_word == endWord:
                        return level + 1
                    # If the next_word is in the wordSet, add it to the queue
                    if next_word in wordSet:
                        queue.append((next_word, level + 1))
                        wordSet.remove(next_word)  # Remove to avoid revisiting

        # Return 0 if there is no possible transformation
        return 0