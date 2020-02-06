'''
1283. Find the Smallest Divisor Given a Threshold

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums) + 1
        value = 0
        while left < right:
            mid = (right - left) // 2 + left
            #if sum(val // mid + (val % mid != 0) for val in nums) > threshold:
            if sum((val + mid - 1) // mid for val in nums) > threshold:
                left = mid + 1
            else:
                right = mid
        return left
