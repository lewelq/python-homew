class Matrix:
    data = []
    def __init__(self, rows, cols):
        #data = ['0'.split("',") * cols] * rows
        self.rows = rows
        self.cols = cols
        Matrix.data = [[0 for i in range(cols)] for j in range(rows)]
        print(self.data)

    def __eq__(self, other):
        pass
        #ИСПРАВИТЬ
        #return self.rows == other.rows and self.cols == other.cols
    
    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            #print(new_matrix)
            #new_matrix = self.data + other.data
            #return new_matrix
            for i in range (self.rows):
                for j in range (self.cols):
                    new_matrix.data = self.data[i][j] + other.data[i][j]
            return new_matrix

matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

print(matrix1 == matrix2)

matrix_sum = matrix1 + matrix2
#print(matrix_sum)