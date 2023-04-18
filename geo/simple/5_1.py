def find_min_max_diagonal(matrix):
    n = len(matrix)
    if n == 0:
        return []

    max_diag = matrix[0][0]
    min_diag = matrix[0][0]

    for i in range(n):
        if matrix[i][i] > max_diag:
            max_diag = matrix[i][i]
        if matrix[i][i] < min_diag:
            min_diag = matrix[i][i]

    if n > 1:
        max_diag2 = matrix[0][n - 1]
        min_diag2 = matrix[0][n - 1]

        for i in range(n):
            if matrix[i][n - 1 - i] > max_diag2:
                max_diag2 = matrix[i][n - 1 - i]
            if matrix[i][n - 1 - i] < min_diag2:
                min_diag2 = matrix[i][n - 1 - i]

        return [min(min_diag, min_diag2), max(max_diag, max_diag2)]

    return [min_diag, max_diag]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(find_min_max_diagonal(matrix))
