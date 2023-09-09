#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        if element == row[-1]:
            print(element, end='')
        else:
            print(element, end=" ")
    print("$")






def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element == row[-1]:
                print(element, end='')
            else:
                print(element, end=" ")
        print("$")
