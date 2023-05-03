from .rtweekend import clamp
from .vec3 import Color


def write_color(pixel_color: Color, samples_per_pixel: int) -> str:
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Divide color by number of samples and gamma-correct for gamma=2.0
    scale = 1.0 / samples_per_pixel

    gamma = 2.0
    r = pow(scale * r, 1/gamma)
    g = pow(scale * g, 1/gamma)
    b = pow(scale * b, 1/gamma)

    # Write the tranlates [0, 255] value of each color component
    return (
        f'{int(256 * clamp(r, 0.0, 0.999))}'
        ' '
        f'{int(256 * clamp(g, 0.0, 0.999))}'
        ' '
        f'{int(256 * clamp(b, 0.0, 0.999))}'
        '\n'
    )
