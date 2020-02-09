'''
Leetcode 664 Strange Printer

There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.

Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.
'''


class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + 1
                    for k in range(i + 1, j + 1):
                        if s[k] == s[i]:
                            dp[i][j] = min(dp[i][j], dp[i + 1][k] + (dp[k + 1][j] if k + 1 <= j else 0))
        return dp[0][-1]
