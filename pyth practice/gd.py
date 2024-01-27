class Matrix:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [['0'] * cols for _ in range(rows)]

    def __eq__(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.data[i][j] = str(int(self.data[i][j]) + int(other.data[i][j]))
            return new_matrix
        else:
            return "Matrices are not of the same size"

matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

print(matrix1 == matrix2)

matrix_sum = matrix1 + matrix2

print(matrix_sum)