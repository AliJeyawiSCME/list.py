import random

matrix = []
numberOfRows = eval(input("Enter number of rows: "))
numberOfColumns = eval(input("Enter number of columns: "))
for row in range(0, numberOfRows):
    matrix.append([])
    for columns in range(0, numberOfColumns):
        matrix[row].append(random.randrange(0, 100))
print(matrix)