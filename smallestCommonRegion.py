'''

leetcode 1257 Smallest Common Region

You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a region X contains itself.

Given two regions region1, region2, find out the smallest region that contains both of them.

If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It's guaranteed the smallest region exists.

'''

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        def find_common_smallest(root):
            mask = 0
            if root == region1:
                mask |= 1
            elif root == region2:
                mask |= 2
            for child in graph[root]:
                ret, mask2 = find_common_smallest(child)
                mask |= mask2
                if mask == 3:
                    return ret if ret else root, mask
            return None, mask

        # build graph
        graph = collections.defaultdict(list)
        non_roots = set()
        for regions_one in regions:
            root = regions_one[0]
            for i in range(1, len(regions_one)):
                graph[root].append(regions_one[i])
                non_roots.add(regions_one[i])

        # find smallest comon region from nodes with no incoming edges
        roots = [root for root in graph if root not in non_roots]
        for root in roots:
            common, _ = find_common_smallest(root)
            if common:
                return common
        return None
