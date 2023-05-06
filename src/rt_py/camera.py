from decimal import Decimal
from .vec3 import Point3, Vec3
from .ray import Ray


class Camera:
    def __init__(self) -> None:
        self.aspect_ratio = Decimal(16.0 / 9.0)
        self.viewport_height = Decimal(2.0)
        self.viewport_width = self.aspect_ratio * self.viewport_height
        self.focal_length = Decimal(1.0)

        self.origin = Point3(Decimal(0), Decimal(0), Decimal(0))
        self.horizontal = Vec3(self.viewport_width, Decimal(0.0), Decimal(0.0))
        self.vertical = Vec3(Decimal(0.0), self.viewport_height, Decimal(0.0))
        self.lower_left_corner = (
            self.origin
            - (self.horizontal / Decimal(2))
            - (self.vertical / Decimal(2))
            - Vec3(0, 0, self.focal_length)
        )

    def get_ray(self, u: Decimal, v: Decimal) -> Ray:
        return Ray(
            self.origin,
            self.lower_left_corner
            + (u * self.horizontal)
            + (v * self.vertical)
            - self.origin,
        )
