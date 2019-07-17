class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]
        for i in range(1, n): 
            fac.append(fac[-1] * i)
        fac.reverse()
        
        digits = [str(x) for x in range(1, n+1)]
        
        num = ""
        k -= 1
        for i in range(n):
            mok, remain = divmod(k, fac[i]) 
            k = remain
            val = digits[mok]
            num += val
            digits.remove(val)

        return num