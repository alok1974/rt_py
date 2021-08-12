from .hittable import Hittable
from .vec3 import Vec3


class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, r, t_min, t_max, rec):
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

        return True
