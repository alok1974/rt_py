from decimal import Decimal
import random


def random_double(minimum: Decimal, maximum: Decimal) -> Decimal:
    """Returns a random real in [min, max)"""
    return minimum + (maximum - minimum) * Decimal(random.random())


def clamp(x: Decimal, minimum: Decimal, maximum: Decimal) -> Decimal:
    if x < minimum:
        return minimum

    if x > maximum:
        return maximum
    return x
