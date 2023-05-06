from abc import ABC, abstractmethod


from decimal import Decimal

from .vec3 import Vec3, Point3
from .ray import Ray


class HitRecord:
    def __init__(self) -> None:
        self.p = Point3()
        self.normal = Vec3()
        self.t = Decimal(0.0)
        self.front_face = False
        self.material = None

    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        front_face = Vec3.dot(r.direction, outward_normal) < Decimal(0)
        self.normal = outward_normal if front_face else -outward_normal


class Hittable(ABC):
    @abstractmethod
    def hit(r: Ray, t_min: Decimal, t_max: Decimal, rec: HitRecord) -> bool:
        ...
