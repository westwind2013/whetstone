import functools
import math

class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:

        @functools.lru_cache(maxsize=None)
        def dp(i):
            if i >= len(A) or A[i] == -1:
                return math.inf
            elif i == len(A) - 1:
                return A[i]
            res = math.inf
            for j in range(i + 1, i + B + 1):
                tmp = dp(j) + A[i]
                if tmp < res:
                    paths[i] = j
                    res = tmp
            return res

        paths = [math.inf for _ in range(len(A))]
        if math.isclose(dp(0), math.inf):
            return []
        res = []
        i = 0
        while i != len(A) - 1:
            res.append(i + 1)
            i = paths[i]
        res.append(len(A))
        return res
