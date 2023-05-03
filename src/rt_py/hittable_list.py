from .hittable import Hittable, HitRecord
from .ray import Ray


class HittableList(Hittable):
    def __init__(self, hittable_object: Hittable = None) -> None:
        self._objects = []
        if hittable_object is not None:
            self.add(hittable_object)

    def clear(self) -> None:
        self._objects.clear()

    def add(self, hittable_object) -> None:
        self._objects.append(hittable_object)

    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for hittable_object in self._objects:
            if hittable_object.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.t = temp_rec.t
                rec.front_face = temp_rec.front_face

        return hit_anything
