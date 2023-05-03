import random


def random_double(minimum: float, maximum: float) -> float:
    """Returns a random real in [min, max)"""
    return minimum + (maximum - minimum) * random.random()


def clamp(x: float, minimum: float, maximum: float) -> float:
    if x < minimum:
        return minimum

    if x > maximum:
        return maximum
    return x
