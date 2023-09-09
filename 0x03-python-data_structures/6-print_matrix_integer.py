#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element == row[-1]:
                print(element, end='')
            else:
                print(element, end=" ")
        print("$")
