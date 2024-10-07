from typing import *
from functools import *

type Vector = Vector
type VectorCompatible = Union[Vector, int]

def zero(dimension: int) -> Vector:
    return Vector([0 for _ in range(dimension)])

def unit(dimension: int, order: int) -> Vector:
    coords = [0 for _ in range(dimension)]
    coords[order] = 1
    return Vector(coords)

class Vector:
    def __init__(self, coords:list[float]) -> None:
        """Create a Vector Object of dimension n with real number as coordinates"""
        self.coords = tuple([coord for coord in coords])
    
    def __len__(self) -> int:
        return len(self.coords)
    
    def __repr__(self) -> str:
        """Return the str representation of the Vector"""
        return "vector" + str(len(self)) + "(" + ", ".join(str(c) for c in self.coords) + ")"

    def __add__(self, vect: Vector) -> Vector:
        """Add two vector with the same dimension"""
        try:
            if type(vect) != type(self):
                raise Exception("Cannot add Vector with " + type(vect))
            elif len(self) != len(vect):
                raise Exception("Cannot add two vector with differents dimensions (" + str(len(self)) + " and " + str(len(vect)) + ")")
            else:
                return Vector([a+b for a, b in zip(self.coords, vect.coords)])
        except:
            return self

    def __radd__(self, vect: Vector) -> Vector:
        """Add two vector with the same dimension"""
        return self.__add__(vect)

    def __mul__(self, vect: VectorCompatible) -> VectorCompatible:
        """Multiply a vector with a scalar or another vector with the same dimension"""
        try:
            if type(vect) == type(self):
                if len(vect) != len(self):
                    raise Exception("Cannot multiply two vector with differents dimensions (" + str(len(self)) + " and " + str(len(vect)) + ")")
                else:
                    return sum([a*b for a, b in zip(self.coords, vect.coords)])
            else:
                return Vector([vect*c for c in self.coords])
        except:
            return self
    
    def __rmul__(self, vect: VectorCompatible) -> VectorCompatible:
        """Multiply a vector with a scalar or another vector with the same dimension"""
        return self.__mul__(vect)
    
    def __abs__(self) -> float:
        """Return the absolute value (norma) of the vector"""
        return (sum([c**2 for c in self.coords]))**.5

    def __eq__(self, vect: Vector) -> bool:
        """Check if two vectors are equals or not"""
        try:
            return not sum([a != b for a, b in zip(self.coords, vect.coords)])
        except:
            return False

    def __neq__(self, vect: Vector) -> bool:
        """Check if two vectors are differents or not"""
        return not self.__eq__(vect)

    def extend_dimension(self, new_size: int) -> Vector:
        """Extend or truncate the vector to another dimension"""
        if len(self) >= new_size:
            self.coords = self.coords[:new_size]
        else:
            dim_gap = new_size-len(self)
            self.coords.extend([0 for _ in range(dim_gap)])
    
    def __list__(self):
        return self.coords
    
    def __tuple__(self):
        return tuple(self.coords)

    def __set__(self):
        return set(self.coords)

    def __dict__(self):
        return {axes:coord for axes, coord in enumerate(self.coords)}