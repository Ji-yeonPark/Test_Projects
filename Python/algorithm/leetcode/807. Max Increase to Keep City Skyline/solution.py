class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        _col = [max(col) for col in zip(*grid)]
        _row = [max(row) for row in grid]
        
        cnt =0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                cnt += min(_col[j], _row[i]) - num
        return cnt
