class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = [0 for _ in xrange(len(A))]
        
        even = 0
        odd = 1
        for v in A:
            if v % 2 == 0: 
                B[even] = v
                even += 2
            elif v % 2 == 1:
                B[odd] = v
                odd += 2
        return B