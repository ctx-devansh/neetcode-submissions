class NumMatrix:

    prefix_sums = None
    
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix_sums = [([0]*cols) for _ in range(rows)]
        i = 0
        while i < rows:
            running_sum = 0
            j = 0
            while j < cols:
                running_sum += matrix[i][j]
                self.prefix_sums[i][j] = running_sum
                j += 1
            i += 1

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        box_sum = 0
        for i in range(row1,row2+1):
            if col1 > 0:
                box_sum += self.prefix_sums[i][col2] - self.prefix_sums[i][col1-1]
            else:
                box_sum += self.prefix_sums[i][col2]
        return box_sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)