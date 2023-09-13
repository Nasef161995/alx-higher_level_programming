#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new = [[pow(element, 2) for element in row] for row in matrix]

print(new)
print(matrix)
