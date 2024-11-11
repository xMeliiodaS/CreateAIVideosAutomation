import random


def generate_random_number(min_value, max_value):
    """
    Generates a random number between min_value and max_value (inclusive).

    Parameters:
    min_value (int): The minimum value of the range.
    max_value (int): The maximum value of the range.

    Returns:
    int: A random number within the given range.
    """
    return random.randint(min_value, max_value)
