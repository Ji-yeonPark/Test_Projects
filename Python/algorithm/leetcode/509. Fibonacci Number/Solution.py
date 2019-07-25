class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1: return N
        
        first = 0
        second = 1
        for i in range(2, N+1):
            third = first + second
            first = second
            second = third
        return second