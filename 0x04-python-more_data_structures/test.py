#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new = [i for i in matrix]
print(matrix)
print(new)

for i in range(3):
    for j in range(3):
        new[i][j] = new[i][j]**2

print(new)
print(matrix)
print('=======================')
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element)
new = [[i**2 for i in x] for x in matrix]
print(new)
print(matrix)
print('=======================')
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
my_list[0] = []
print(my_list)
