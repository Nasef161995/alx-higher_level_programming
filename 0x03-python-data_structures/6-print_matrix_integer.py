#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for a in range(len(matrix)):
            for b in range(len(matrix)):
                if b < len(matrix) - 1:
                    print("{:d}".format(matrix[a][b]), end=' ')
                elif b == len(matrix) - 1:
                    print("{:d}".format(matrix[a][b]), end='')
            else:
                print("$")
