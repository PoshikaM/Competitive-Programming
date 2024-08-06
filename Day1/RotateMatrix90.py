def rotate_matrix_90_degree_clockwise(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]
    
    return rotated_matrix

def input_matrix(n):
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").strip().split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

n = int(input("Enter the size of the matrix (n x n): "))
matrix = input_matrix(n)

rotated = rotate_matrix_90_degree_clockwise(matrix)
print("Rotated matrix:")
print_matrix(rotated)