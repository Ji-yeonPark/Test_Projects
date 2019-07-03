class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l = []
        for i in range(num+1):
            l.append(bin(i)[2:].count('1'))
        return l