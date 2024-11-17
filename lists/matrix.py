import random

matrix = []
numberOfRows = eval(input("Enter number of rows: "))
numberOfColumns = eval(input("Enter number of columns: "))
for row in range(0, numberOfRows):
    matrix.append([])
    for columns in range(0, numberOfColumns):
        matrix[row].append(random.randrange(0, 100))
print(matrix)

# total = 0
# for row in range(0, len(matrix)):
#     for column in range(0, len(matrix[row])):
#         total += matrix[row][column]
# print("Total is " + str(total))

total = 0
for column in range(0, len(matrix[0])):
    for row in range(0, len(matrix)):
        total += matrix[row][column]
    print("Column sum " + str(column), "is " + str(total))