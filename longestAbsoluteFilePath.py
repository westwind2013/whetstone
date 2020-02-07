'''
388. Longest Absolute File Path
'''

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        length = 0
        for raw in input.split('\n'):
            count = 0
            for i, c in enumerate(raw):
                if c != '\t':
                    count = i
                    break
            name_length = len(raw) - count
            while len(stack) > count:
                stack.pop()
            stack.append(name_length + 1 + (stack[-1] if stack else 0))
            if '.' in raw[count:]:
                length = max(length, stack[-1] - 1)
        return length


