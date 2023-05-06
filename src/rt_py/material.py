from abc import ABC, abstractmethod
from typing import Tuple


from .hittable import HitRecord
from .ray import Ray
from .vec3 import Color, Vec3


class Material(ABC):
    @abstractmethod
    def scatter(self, r_in: Ray, rec: HitRecord) -> Tuple[bool, Ray, Color]:
        ...


class Lambertian(Material):
    def __init__(self, albedo: Color):
        self.albedo = albedo

    def scatter(self, r_in: Ray, rec: HitRecord) -> Tuple[bool, Ray, Color]:
        scatter_direction = rec.normal + Vec3.random_unit_vector()
        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction)
        attenuation = self.albedo
        return True, scattered, attenuation


class Metal:
    def __init__(self, albedo: Color) -> None:
        self.albedo = albedo

    def scatter(self, r_in: Ray, rec: HitRecord) -> Tuple[bool, Ray, Color]:
        reflected = Vec3.reflect(
            Vec3.unit_vector(r_in.direction),
            rec.normal,
        )
        scattered = Ray(rec.p, reflected)
        attenuation = self.albedo
        return Vec3.dot(scattered.direction, rec.normal) > 0, scattered, attenuation
