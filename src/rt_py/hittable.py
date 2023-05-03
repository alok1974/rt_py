from abc import ABC, abstractmethod


from .vec3 import Vec3, Point3
from .ray import Ray


class HitRecord:
    def __init__(self) -> None:
        self.p = Point3()
        self.normal = Vec3()
        self.t = 0.0
        self.front_face = False

    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        front_face = Vec3.dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if front_face else -outward_normal


class Hittable(ABC):
    @abstractmethod
    def hit(r: Ray, t_min: float, t_max: float, rec: HitRecord):
        ...
