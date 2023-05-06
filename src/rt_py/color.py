from .rtweekend import clamp


def write_color(pixel_color, samples_per_pixel):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Divide color by number of samples
    scale = 1.0 / samples_per_pixel

    r *= scale
    g *= scale
    b *= scale

    # Write the tranlates [0, 255] value of each color component
    return (
        f'{int(256 * clamp(r, 0.0, 0.999))}'
        ' '
        f'{int(256 * clamp(g, 0.0, 0.999))}'
        ' '
        f'{int(256 * clamp(b, 0.0, 0.999))}'
        '\n'
    )
