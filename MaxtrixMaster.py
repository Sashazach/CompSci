class MatrixMaster:
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def plus(self, matrix : 'MatrixMaster') -> 'MatrixMaster':
        if matrix.rows != self.rows or matrix.cols != self.cols: return
        newMatrix = MatrixMaster(self.rows, self.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                newMatrix.data[i][j] = matrix.data[i][j] + self.data[i][j]
        return newMatrix
            
    def multiply(self, matrix : 'MatrixMaster') -> 'MatrixMaster':
        newMatrix = MatrixMaster(self.rows, matrix.cols)
        for i in range(self.rows):
            for j in range(matrix.cols):
                for k in range(self.cols):
                    newMatrix.data[i][j] = self.data[i][k]*matrix.data[k][j]
        return newMatrix
    
    def print_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j], end="")
            print()
    
    def scalarTimesRow(self, scalar, rownumber):
        if 0 <= rownumber <= self.rows:
            for i in range(self.cols):
                self.data[rownumber][i] = self.data[rownumber][i] * scalar

    def switchRows(self, firstRow, secondRow):
        self.data[firstRow], self.data[secondRow] = self.data[secondRow], self.data[firstRow]

    def linearCombRows(self, scalar, firstRow, secondRow):
        if 0 <= firstRow < self.rows and 0 <= secondRow < self.rows:
            for i in range(self.cols):
                self.data[firstRow][i] = scalar * self.data[firstRow][i] + self.data[secondRow][i]
        else:
            raise IndexError("Row number out of range!")