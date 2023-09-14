def transpon(matrix):
    trans_matrix = []
    for j in range(len(matrix[1])):
        trans_matrix.append([])
        for i in range(len(matrix)):
            trans_matrix[j].append(matrix[i][j])
    return (f"\n{trans_matrix[0]}\n{trans_matrix[1]}\n{trans_matrix[2]}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"оригинальная матрица:\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}" )
print(f"транспонированная матрица:{transpon(matrix)}")