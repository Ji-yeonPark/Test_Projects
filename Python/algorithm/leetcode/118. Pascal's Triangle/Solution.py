class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tree = []
        for n in range(1, numRows+1):
            tmp = [0 for _ in range(n)]
            tmp[0] = tmp[-1] = 1
            
            i = 0   
            while tmp.count(0) > 0:
                tmp[i+1] = tree[-1][i] + tree[-1][i+1]  
                i += 1
            tree.append(tmp)
        return tree