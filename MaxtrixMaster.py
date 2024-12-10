# Author - Zach Bostock
# Title - Matrix Assignment
# Created Novemeber 2024
# Included project components - all required functions + REF

class MatrixMaster:
    def __init__(self, rows, cols):
        # create class instance with set rows and cols
        self.cols = cols
        self.rows = rows
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def plus(self, matrix : 'MatrixMaster') -> 'MatrixMaster':
        if matrix.rows != self.rows or matrix.cols != self.cols:
            raise ValueError("Cannot add: Matrices must have the same dimensions.")
        newMatrix = MatrixMaster(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                newMatrix.data[i][j] = self.data[i][j] + matrix.data[i][j]
        return newMatrix
            
    def multiply(self, matrix : 'MatrixMaster') -> 'MatrixMaster':
        if self.cols != matrix.rows:
            raise ValueError("Cannot multiply: Incompatible matrix dimensions.")
        newMatrix = MatrixMaster(self.rows, matrix.cols)
        for i in range(self.rows):
            for j in range(matrix.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * matrix.data[k][j]
                newMatrix.data[i][j] = sum
        return newMatrix
    
    def print_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(f"{self.data[i][j]:.2f}", end="\t")
            print()
    
    def scalarTimesRow(self, scalar, rownumber):
        if 0 <= rownumber < self.rows:
            for i in range(self.cols):
                self.data[rownumber][i] *= scalar
        else:
            raise IndexError("Row number out of range!")

    def switchRows(self, firstRow, secondRow):
        if 0 <= firstRow < self.rows and 0 <= secondRow < self.rows:
            self.data[firstRow], self.data[secondRow] = self.data[secondRow], self.data[firstRow]
        else:
            raise IndexError("Row number out of range!")

    def linearCombRows(self, scalar: float, sourceRow: int, targetRow: int):
        if 0 <= sourceRow < self.rows and 0 <= targetRow < self.rows:
            for i in range(self.cols):
                self.data[targetRow][i] += scalar * self.data[sourceRow][i]
        else:
            raise IndexError("Row numbers are not within the valid range!")
    
    def ref(self):
        # convert to row echelon form (REF)
        n = min(self.rows, self.cols)
                
        for i in range(n):
            # find pivot
            pivot_row = None
            for row in range(i, n):
                if self.data[row][i] != 0:
                    pivot_row = row
                    break

            if pivot_row is None:
                continue

            if pivot_row != i: 
                self.switchRows(i, pivot_row)

            # eliminate below pivot
            for row in range(i + 1, n):
                factor = self.data[row][i]
                if factor != 0:
                    self.linearCombRows(-factor / self.data[i][i], i, row)

    def invert(self):
        if self.rows != self.cols:
            raise ValueError("Only square matrices can be inverted. This is not one!")

        n = self.rows

        identity = MatrixMaster(n, n) # store an identity matrix with NxN dimensions in the 'identity' variable
        for i in range(n):
            identity.data[i][i] = 1.0 # initialize the diagonol values of the identity matrix to 1

        augmented = MatrixMaster(n, n * 2) # create an augmented matrix with twice the number of collumns
        for i in range(n): 
            augmented.data[i] = self.data[i] + identity.data[i] # concatenate the rows of the matrix and the identity matrix

        for i in range(n):
            pivot = augmented.data[i][i]
            if pivot == 0:
                for j in range(i + 1, n): # loop through rows to find one with a non-zero coefficient for the i'th column
                    if augmented.data[j][i] != 0:
                        augmented.switchRows(i, j) # switch rows if non-zero coefficient is found in the i'th column
                        pivot = augmented.data[i][i] # set the new pivot point
                        break
                else:
                    raise ValueError("Matrix has determinant of zero and is not invertible.")

            augmented.scalarTimesRow(1 / pivot, i) # normalize the pivot row

            
            for k in range(n): # eliminate all other entries in the pivot column given pivot is normalized
                if k != i:
                    factor = augmented.data[k][i]
                    augmented.linearCombRows(-factor, i, k)

        # take out the inverse matrix from the augmented matrix
        inverse_matrix = MatrixMaster(n, n)
        for i in range(n):
            inverse_matrix.data[i] = augmented.data[i][n:]

        return inverse_matrix

    def transpose(self):
        # return the transposed matrix
        transposed = MatrixMaster(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def rowReduce(self):
        # Start by producing REF form
        self.ref()

        n = min(self.rows, self.cols)

        # Convert REF to RREF by eliminating above pivots and ensuring pivots are 1
        for i in range(n - 1, -1, -1):
            pivot_col = None
            # find first nonzero entry in row as pivot
            for j in range(self.cols):
                if self.data[i][j] != 0:
                    pivot_col = j
                    break

            if pivot_col is None:
                continue

            # normalize pivot to 1
            pivot = self.data[i][pivot_col]
            if pivot != 1:
                self.scalarTimesRow(1 / pivot, i)

            # eliminate above pivot
            for row in range(i):
                factor = self.data[row][pivot_col]
                if factor != 0:
                    self.linearCombRows(-factor, i, row)