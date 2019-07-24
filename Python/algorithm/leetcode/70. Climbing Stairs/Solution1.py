class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb(0, n)
        
    def climb(self, i, n):
        if i > n: return 0
        elif i == n: return 1
        return self.climb(i+1, n) + self.climb(i+2, n)