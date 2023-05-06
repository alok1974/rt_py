from __future__ import annotations

from decimal import Decimal
import math
import random

from .rtweekend import random_double


class Vec3:
    def __init__(self, e0: Decimal = 0.0, e1: Decimal = 0.0, e2: Decimal = 0.0) -> None:
        self.e = [Decimal(e0), Decimal(e1), Decimal(e2)]

    def x(self) -> Decimal:
        return self.e[0]

    def y(self) -> Decimal:
        return self.e[1]

    def z(self) -> Decimal:
        return self.e[2]

    def __neg__(self) -> Vec3:
        cls = self.__class__
        return cls(
            -1 * self.e[0],
            -1 * self.e[1],
            -1 * self.e[2],
        )

    def __getitem__(self, key: int) -> Decimal:
        return self.e[key]

    def __add__(self, other: int | Decimal | Vec3) -> Vec3:
        if isinstance(other, (int, Decimal)):
            e0 = self.e[0] + Decimal(other)
            e1 = self.e[1] + Decimal(other)
            e2 = self.e[2] + Decimal(other)
        elif isinstance(other, Vec3):
            e0 = self.e[0] + other.e[0]
            e1 = self.e[1] + other.e[1]
            e2 = self.e[2] + other.e[2]
        else:
            raise ValueError(f'Cannot add {type(other)} to {type(self)}')

        return self.__class__(e0, e1, e2)

    def __radd__(self, other: Vec3) -> Vec3:
        return self + other

    def __sub__(self, other: int | Decimal | Vec3) -> Vec3:
        if isinstance(other, (int, Decimal)):
            e0 = self.e[0] - Decimal(other)
            e1 = self.e[1] - Decimal(other)
            e2 = self.e[2] - Decimal(other)
        elif isinstance(other, Vec3):
            e0 = self.e[0] - other.e[0]
            e1 = self.e[1] - other.e[1]
            e2 = self.e[2] - other.e[2]
        else:
            raise ValueError(f'Cannot add {type(other)} to {self}')

        return self.__class__(e0, e1, e2)

    def __mul__(self, other: int | Decimal | Vec3) -> Vec3:
        if isinstance(other, (int, Decimal)):
            e0 = self.e[0] * Decimal(other)
            e1 = self.e[1] * Decimal(other)
            e2 = self.e[2] * Decimal(other)
        elif isinstance(other, Vec3):
            e0 = self.e[0] * other.e[0]
            e1 = self.e[1] * other.e[1]
            e2 = self.e[2] * other.e[2]
        else:
            raise ValueError(f'Cannot multiply {type(other)} to {type(self)}')

        return self.__class__(e0, e1, e2)

    def __rmul__(self, other: Vec3) -> Vec3:
        return self * other

    def __truediv__(self, other: int | Decimal) -> Vec3:
        if not isinstance(other, (int, Decimal)):
            raise ValueError(f'Cannot divide {type(other)} to {type(self)}')

        return self.__class__(
            self.e[0] / Decimal(other),
            self.e[1] / Decimal(other),
            self.e[2] / Decimal(other),
        )

    def length_squared(self) -> Decimal:
        return (
            (self.e[0] * self.e[0])
            + (self.e[1] * self.e[1])
            + (self.e[2] * self.e[2])
        )

    def length(self) -> Decimal:
        return Decimal(math.sqrt(self.length_squared()))

    def __repr__(self) -> str:
        return f'{self.e[0]}, {self.e[1]}, {self.e[2]}'

    @staticmethod
    def dot(u: Vec3, v: Vec3) -> Decimal:
        return (
            (u.e[0] * v.e[0])
            + (u.e[1] * v.e[1])
            + (u.e[2] * v.e[2])
        )

    @staticmethod
    def cross(u: Vec3, v: Vec3) -> Vec3:
        cls = u.__class__
        return cls(
            e0=(u.e[1] * v.e[2]) - (u.e[2] * v.e[1]),
            e1=(u.e[2] * v.e[0]) - (u.e[0] * v.e[2]),
            e2=(u.e[0] * v.e[1]) - (u.e[1] * v.e[0]),
        )

    @staticmethod
    def unit_vector(v: Vec3) -> Vec3:
        return v / v.length()

    @classmethod
    def random(cls) -> Vec3:
        return cls(
            Decimal(random.random()),
            Decimal(random.random()),
            Decimal(random.random()),
        )

    @classmethod
    def random_min_max(cls, minimum: Decimal, maximum: Decimal) -> Vec3:
        return cls(
            Decimal(random_double(minimum, maximum)),
            Decimal(random_double(minimum, maximum)),
            Decimal(random_double(minimum, maximum)),
        )

    @classmethod
    def random_in_unit_sphere(cls) -> Vec3:
        while True:
            p = cls.random_min_max(Decimal(-1.0), Decimal(1))
            if p.length_squared() >= 1:
                continue
            return p

    @classmethod
    def random_unit_vector(cls) -> Vec3:
        return cls.unit_vector(cls.random_in_unit_sphere())

    @classmethod
    def random_in_hemisphere(cls, normal: Vec3) -> Vec3:
        in_unit_sphere = cls.random_in_unit_sphere()
        if cls.dot(in_unit_sphere, normal) > 0.0:
            return in_unit_sphere
        else:
            return -in_unit_sphere

    def near_zero(self) -> bool:
        s = Decimal('1e-8')
        return (
            math.fabs(self.e[0]) < s
            and math.fabs(self.e[1]) < s
            and math.fabs(self.e[2]) < s
        )

    @staticmethod
    def reflect(v: Vec3, n: Vec3) -> Vec3:
        return v - 2 * Vec3.dot(v, n) * n


Point3 = Vec3
Color = Vec3
