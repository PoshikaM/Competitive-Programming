def generate_pascals_triangle(num_rows):
    triangle = []
    
    for i in range(num_rows):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)
    
    return triangle

rows = 5
triangle = generate_pascals_triangle(rows)
for row in triangle:
    print(row)