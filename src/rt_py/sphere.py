from .hittable import Hittable, HitRecord
from .vec3 import Vec3, Point3
from .ray import Ray
from .material import Material


class Sphere(Hittable):
    def __init__(self, center: Point3, radius: float, material: Material) -> None:
        self.center = center
        self.radius = radius
        self.material = material

    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = Vec3.dot(oc, r.direction)
        c = oc.length_squared() - (self.radius * self.radius)

        discriminant = (half_b * half_b) - (a * c)
        if discriminant < 0:
            return False

        sqrtd = pow(discriminant, 0.5)

        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.material = self.material

        return True
