from typing import *
from functools import *

type Matrix = Matrix

def zero(order: int) -> Matrix:
    matrix = []
    for _ in range(order):
        matrix.append([0 for _ in range(order)])
    return Matrix(matrix)

def zero_rect(width: int, height: int) -> Matrix:
    matrix = []
    for _ in range(height):
        matrix.append([0 for _ in range(width)])
    return Matrix(matrix)

def unit(order: int) -> Matrix:
    matrix = []
    for i in range(order):
        line = []
        for j in range(order):
            line.append(0 if i != j else 1)
        matrix.append(line)
    return Matrix(matrix)

class Matrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        try:
            s = len(matrix[0])
            for line in matrix[1:]:
                if s != len(line):
                    raise Exception("Invalid Matrix format (non-rectangular)")
            self.matrix = matrix
        except:
            self.matrix = [[0]]
    
    def __repr__(self) -> str:
        """Return a str representation of the matrix"""
        return "\n".join([" ¦ ".join([str(value) for value in line]) for line in self.matrix]) + "\n"

    def __add__(self, matrix: Matrix):
        try:
            if not self.check_format(matrix):
                raise Exception("Format error, cannot add two matrix of the wrong format")
            else:
                scheme = []
                for line1, line2 in zip(matrix.matrix, self.matrix):
                    scheme.append([a+b for a, b in zip(line1, line2)])
                return Matrix(scheme)
        except:
            return self.matrix
    
    def __radd__(self, matrix: Matrix) -> Matrix:
        return self.__add__(matrix)

    def __mul__(self, matrix: Union[Matrix, int]) -> Matrix:
        if type(matrix) is int:
            scheme = []
            for line in self.matrix:
                scheme.append([matrix*v for v in line])
            return Matrix(scheme)
        if type(matrix) == type(self):
            if not self.check_format(matrix):
                raise Exception("Format error, cannot add two matrix of the wrong format")
            else:
                scheme = []
                for line1, line2 in zip(self.matrix, matrix.matrix.transpose()):
                    line = []
                    s = 0
                    for v1, v2 in zip(line1, line2):
                        s += v1*v2
                    line.append(s)
                    scheme.append(line)
                return Matrix(scheme)
        
    
    def get_width(self):
        return len(self.matrix[0])

    def get_height(self):
        return len(self.matrix)

    def transpose(self) -> Matrix:
        """Return the transpose of the matrix"""
        matrix = []
        for x in range(len(self.matrix[0])):
            line = []
            for y in range(len(self.matrix)):
                line.append(self.matrix[y][x])
            matrix.append(line)
        return Matrix(matrix)

    def trace(self) -> int:
        if self.get_format()[0] != self.get_format()[1]:
            raise Exception("The matrix is not square")
        else:
            return sum([self.matrix[i][i] for i in range(len(self.matrix))])

    def check_format(self, matrix: Matrix) -> bool:
        if len(matrix.matrix) != len(self.matrix):
            return False
        for line1, line2 in zip(matrix.matrix, self.matrix):
            if len(line1) != len(line2):
                return False
        return True

    def get_format(self) -> tuple:
        return (len(self.matrix), len(self.matrix[0]))