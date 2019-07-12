class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        
        check = [[0 for _ in range(n)] for _ in range(n)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        
        i = j = di = 0
        for num in range(1, (n * n)+1):            
            check[i][j] = num
            
            _x, _y = i + direction[di][0], j + direction[di][1]
            if 0 <= _x < n and 0 <= _y < n and check[_x][_y] == 0:
                i, j = _x, _y
            else:  # 방향 변경
                di = (di + 1) % 4
                i, j = i + direction[di][0], j + direction[di][1]
        return check