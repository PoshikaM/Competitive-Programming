row = int(input())
col = int(input())
matrix1 = []
matrix2 = []

for i in range(row):
    a = list(map(int, input().split()))
    matrix1.append(a)

top = 0
bottom = row - 1
left = 0
right = col - 1
count = 0

while count < row * col:
    for i in range(left, right + 1):
        if count < row * col:
            matrix2.append(matrix1[top][i])
            count += 1
    top += 1

    for i in range(top, bottom + 1):
        if count < row * col:
            matrix2.append(matrix1[i][right])
            count += 1
    right -= 1

    for i in range(right, left - 1, -1):
        if count < row * col:
            matrix2.append(matrix1[bottom][i])
            count += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        if count < row * col:
            matrix2.append(matrix1[i][left])
            count += 1
    left += 1

print(matrix2)