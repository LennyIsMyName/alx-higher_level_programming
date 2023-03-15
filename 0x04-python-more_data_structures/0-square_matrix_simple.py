#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [[x*x for x in row] for row in matrix]


'''
def square_matrix_simple(matrix=[]):
    new = list()
    for sublist in matrix:
        row = []
        for item in sublist:
            row.append(item ** 2)
        new.append(row)
    return new
    '''
