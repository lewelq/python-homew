class Matrix:
    data = []
    def __init__(self, rows, cols):
        #data = ['0'.split("',") * cols] * rows
        self.rows = rows
        self.cols = cols
        Matrix.data = [[0 for i in range(cols)] for j in range(rows)]
        data = self.data
        print(self.data)

matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]