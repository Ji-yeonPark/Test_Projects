class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = [0 for _ in range(n+1)]
        total[0] = total[1] = 1
        for i in range(2, n+1):
            total[i] = 0;
            for j in range(1, i+1) :
                total[i] += total[j-1] * total[i-j]
        
        return total[n]
        