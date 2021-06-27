""" Uma classe simples de vetor bidimensional """
from __future__ import annotations
from math import hypot


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        x: int = self.x + other.x
        y: int = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar: int) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)
