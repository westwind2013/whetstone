'''
Leetcode
1338. Reduce Array Size to The Half

Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
'''

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts_map = collections.Counter()
        for a in arr:
            counts_map[a] += 1
        counts = sorted(counts_map.values(), reverse=True)
        target = len(arr) // 2
        count = 0
        for val in counts:
            target -= val
            count += 1
            if target <= 0:
                break
        return count

