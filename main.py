print("Laboratorna 1")

ito = 0
jto = 0
print("")
print("i - ряд, j - стовбчик")

ito = int(input("Enter size of i matrix: "))
jto = int(input("Enter size of j matrix: "))

matrix = []

# Fill the matrix with user input
for i in range(ito):
    row = []
    for j in range(jto):
        jtonum = int(input(f"Enter number for row {i + 1}, column {j + 1}: "))
        row.append(jtonum)
    matrix.append(row)

# Display the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Output pairs of orthogonal rows
print("\nOrthogonal Pairs:")
for i in range(ito):
    for j in range(i + 1, ito):
        if all(matrix[i][k] * matrix[j][k] == 0 for k in range(jto)):
            print(f"Row {i + 1} and Row {j + 1} are orthogonal.")


