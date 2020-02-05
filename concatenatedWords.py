"""
leetcode 472

Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def dfs(word, is_start=True):
            if not is_start and word in check:
                return True
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in check and dfs(suffix, False):
                    return True
            return False

        check = set(words)
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res
