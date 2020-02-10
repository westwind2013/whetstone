'''
1074 Number of Submatrices That Sum to Target

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

'''

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        res = 0
        for i in range(len(matrix)):
            cols = [0] * len(matrix[0])
            for j in range(i, len(matrix)):
                avails = collections.Counter()
                avails[0] = 1
                total = 0
                for k in range(len(matrix[0])):
                    cols[k] += matrix[j][k]
                    total += cols[k]
                    if total - target in avails:
                        res += avails[total - target]
                    avails[total] += 1
        return res



