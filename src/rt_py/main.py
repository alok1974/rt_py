import sys


from .vec3 import Color, Point3, Vec3
from .color import write_color
from .ray import Ray


def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = Vec3.dot(r.direction, r.direction)
    b = 2.0 * Vec3.dot(oc, r.direction)
    c = Vec3.dot(oc, oc) - (radius * radius)
    discriminant = b * b - (4 * a * c)
    return discriminant > 0


def ray_color(r):
    if hit_sphere(Point3(0, 0, -1), 0.5, r):
        return Color(1, 0, 0)

    unit_direction = Vec3.unit_vector(r.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return ((1.0 - t) * Color(1.0, 1.0, 1.0)) + (t * Color(0.5, 0.7, 1.0))


def run(image_path):

    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = Point3(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - (horizontal / 2) - (vertical / 2) - Vec3(0, 0, focal_length)

    # Render
    image_data = f'P3\n{image_width} {image_height}\n255\n'

    for j in range(image_height - 1, -1, -1):
        sys.stderr.write(f"\rScanlines reamining: {j} ")
        for i in range(image_width):
            u = float(i) / (image_width - 1)
            v = float(j) / (image_height - 1)
            r = Ray(
                origin=origin,
                direction=(lower_left_corner + (u * horizontal) + (v * vertical) - origin)
            )
            pixel_color = ray_color(r)
            image_data += write_color(pixel_color)
    sys.stderr.write("\nDone.\n")

    with open(image_path, 'w') as fh:
        fh.write(image_data)
