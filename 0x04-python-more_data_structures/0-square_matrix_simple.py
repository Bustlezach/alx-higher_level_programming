#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = [x ** 2 for row in matrix for x in row]
    return square
