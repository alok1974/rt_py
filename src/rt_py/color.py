from decimal import Decimal
import math

from .rtweekend import clamp
from .vec3 import Color


def write_color(pixel_color: Color, samples_per_pixel: int) -> str:
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Divide color by number of samples and gamma-correct for gamma=2.0
    scale = Decimal(1.0 / samples_per_pixel)

    gamma = Decimal(2.0)
    r = Decimal(math.pow(scale * r, Decimal(1)/gamma))
    g = Decimal(math.pow(scale * g, Decimal(1)/gamma))
    b = Decimal(math.pow(scale * b, Decimal(1)/gamma))

    # Write the tranlates [0, 255] value of each color component
    return (
        f'{int(256 * clamp(r, Decimal(0.0), Decimal(0.999)))} '
        f'{int(256 * clamp(g, Decimal(0.0), Decimal(0.999)))} '
        f'{int(256 * clamp(b, Decimal(0.0), Decimal(0.999)))} \n'
    )
