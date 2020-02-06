'''

leetcode 1234. Replace the Substring for Balanced String

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced

'''


class Solution:
    def balancedString(self, s: str) -> int:
        # find the characters that need to be removed, i.e., characters whose count
        # is bigger than len(s) // 4
        counts = sorted([(count, c) for c, count in collections.Counter(s).items()],
                        reverse=True)
        must_have = {}
        for i in range(len(counts)):
            need = counts[i][0] - len(s) // 4
            if need > 0:
                must_have[counts[i][1]] = need
        # sliding window
        length = len(s)
        start = 0
        for i, c in enumerate(s):
            if c not in must_have:
                continue
            must_have[c] -= 1
            while s[start] not in must_have or must_have[s[start]] < 0:
                if s[start] in must_have:
                    must_have[s[start]] += 1
                start += 1
            if all(v <= 0 for v in must_have.values()):
                length = min(length, i - start + 1)
        return length if length < len(s) else 0
