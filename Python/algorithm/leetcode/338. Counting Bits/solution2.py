class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]
        for i in range(1,num+1):
            dp.append(i%2+dp[i/2])
        return dp
