
class Solution(object):
    def heightChecker(self, heights):
        expected = heights[:]
        
        n = len(expected)
        for i in range(n):
            for j in range(0, n - i - 1):
                if expected[j] > expected[j + 1]:
                    expected[j], expected[j + 1] = expected[j + 1], expected[j]
        
        count = 0
        
        for i in range(n):
            if heights[i] != expected[i]:
                count += 1
        
        return count
        