class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if len(row) > 0 and row[0] <= target <= row[-1]:
                while row:
                    num = row.pop()
                    if num == target: return True
                return False
        return False