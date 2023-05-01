import random


def random_double(minimum, maximum):
    """Returns a random real in [min, max)"""
    return minimum + (maximum - minimum) * random.random()


def clamp(x, minimum, maximum):
    if x < minimum:
        return minimum

    if x > maximum:
        return maximum
    return x
