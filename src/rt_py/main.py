import sys
import math
import random


from .vec3 import Color, Point3, Vec3
from .color import write_color
from .hittable import HitRecord
from .hittable_list import HittableList
from .sphere import Sphere
from .camera import Camera
from .ray import Ray
from .material import Lambertian, Metal


def ray_color(r: Ray, world: HittableList, depth: int) -> Color:
    rec = HitRecord()

    # If we've exceeded the ray bounce limit, no more light is gathered
    if depth <= 0:
        return Color(0, 0, 0)

    if world.hit(r, 0, math.inf, rec):
        is_scattered, scaterred, attenuation = rec.material.scatter(r, rec)
        if is_scattered:
            return attenuation * ray_color(scaterred, world, depth - 1)
        return Color(0, 0, 0)

    unit_direction = Vec3.unit_vector(r.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


def run(image_path: str) -> None:
    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 100
    max_depth = 50

    # World
    world = HittableList()

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.7, 0.3, 0.3))
    material_left = Metal(Color(0.8, 0.8, 0.8), 0.3)
    material_right = Metal(Color(0.8, 0.6, 0.2), 1.0)

    world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right))

    # Camera
    cam = Camera()

    # Render
    with open(image_path, 'w') as fh:
        fh.write(f'P3\n{image_width} {image_height}\n255\n')
        for j in reversed(range(image_height)):
            sys.stderr.write(f"\rScanlines reamining: {j} ")
            for i in range(image_width):
                pixel_color = Color(0, 0, 0)
                for _ in range(samples_per_pixel):
                    u = (i + random.random()) / (image_width - 1)
                    v = (j + random.random()) / (image_height - 1)
                    r = cam.get_ray(u, v)
                    pixel_color += ray_color(r, world, max_depth)
                fh.write(write_color(pixel_color, samples_per_pixel))

    sys.stderr.write("\nDone.\n")
