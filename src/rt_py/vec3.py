class Vec3:
    def __init__(self, e0=0.0, e1=0.0, e2=0.0):
        self.e = [float(e0), float(e1), float(e2)]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return self.__class__(
                -1 * self.e[0],
                -1 * self.e[1],
                -1 * self.e[2],
        )

    def __getitem__(self, key):
        return self.e[key]

    def __add__(self, other):
        if not isinstance(other, (int, float, self.__class__)):
            raise ValueError(f'Cannot add {type(other)} to {type(self.__class__)}')

        if isinstance(other, (int, float)):
            e0 = self.e[0] + other
            e1 = self.e[1] + other
            e2 = self.e[2] + other
        else:
            e0 = self.e[0] + other.e[0]
            e1 = self.e[1] + other.e[1]
            e2 = self.e[2] + other.e[2]

        return self.__class__(e0, e1, e2)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, (int, float, self.__class__)):
            raise ValueError(f'Cannot add {type(other)} to {type(self.__class__)}')

        if isinstance(other, (int, float)):
            e0 = self.e[0] - other
            e1 = self.e[1] - other
            e2 = self.e[2] - other
        else:
            e0 = self.e[0] - other.e[0]
            e1 = self.e[1] - other.e[1]
            e2 = self.e[2] - other.e[2]

        return self.__class__(e0, e1, e2)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError(f'Cannot multiply {type(other)} to {type(self.__class__)}')

        return self.__class__(
            self.e[0] * other,
            self.e[1] * other,
            self.e[2] * other,
        )

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError(f'Cannot divide {type(other)} to {type(self.__class__)}')

        return self.__class__(
            self.e[0] / other,
            self.e[1] / other,
            self.e[2] / other,
        )

    def length_squared(self):
        return (self.e[0] * self.e[0]) + (self.e[1] * self.e[1]) + (self.e[2] * self.e[2])

    def length(self):
        return pow(self.length_squared(), 0.5)

    def __repr__(self):
        return f'{self.e[0]}, {self.e[1]}, {self.e[2]}'

    @staticmethod
    def dot(u, v):
        return (u.e[0] * v.e[0]) + (u.e[1] * v.e[1]) + (u.e[2] * v.e[2])

    @staticmethod
    def cross(u, v):
        vec3_class = u.__class__
        return vec3_class(
            e0=(u.e[1] * v.e[2]) - (u.e[2] * v.e[1]),
            e1=(u.e[2] * v.e[0]) - (u.e[0] * v.e[2]),
            e2=(u.e[0] * v.e[1]) - (u.e[1] * v.e[0]),
        )

    @staticmethod
    def unit_vector(v):
        return v / v.length()


Point3 = Vec3
Color = Vec3