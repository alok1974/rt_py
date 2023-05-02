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


def ray_color(r, world, depth):
    rec = HitRecord()

    # If we've exceeded the ray bounce limit, no more light is gathered
    if depth <= 0:
        return Color(0, 0, 0)

    if world.hit(r, 0, math.inf, rec):
        target = rec.p + Vec3.random_in_hemisphere(rec.normal)
        return 0.5 * ray_color(Ray(rec.p, target - rec.p), world, depth - 1)

    unit_direction = Vec3.unit_vector(r.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


def run(image_path):

    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 100
    max_depth = 50

    # World
    world = HittableList()
    world.add(Sphere(Point3(0, 0, -1), 0.5))
    world.add(Sphere(Point3(0, -100.5, -1), 100))

    # Camera
    cam = Camera()

    # Render
    image_data = f'P3\n{image_width} {image_height}\n255\n'

    for j in range(image_height - 1, -1, -1):
        sys.stderr.write(f"\rScanlines reamining: {j} ")

        for i in range(image_width):
            pixel_color = Color(0, 0, 0)

            for _ in range(samples_per_pixel):
                u = (i + random.random()) / (image_width - 1)
                v = (j + random.random()) / (image_height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world, max_depth)

            image_data += write_color(pixel_color, samples_per_pixel)

    sys.stderr.write("\nDone.\n")

    with open(image_path, 'w') as fh:
        fh.write(image_data)
