class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        Row = len(matrix)
        Col = len(matrix[0])
        check = [[0 for _ in matrix[0]] for _ in matrix]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = []
        
        i = j = di = 0
        for _ in range(Row * Col):            
            check[i][j] = True
            result.append(matrix[i][j])

            _x, _y = i + direction[di][0], j + direction[di][1]
            if 0 <= _x < Row and 0 <= _y < Col and not check[_x][_y]:
                i, j = _x, _y
            else:  # 방향 변경
                di = (di + 1) % 4
                i, j = i + direction[di][0], j + direction[di][1]
        return result