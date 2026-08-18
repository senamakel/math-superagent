"""Small exact vector helpers shared by square-peg programs."""
from fractions import Fraction


def Q(x):
    """Convert x to Fraction."""
    return x if isinstance(x, Fraction) else Fraction(x)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(c, a):
    return (c * a[0], c * a[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def on_segment(p, a, b):
    ab = sub(b, a)
    return cross(ab, sub(p, a)) == 0 and dot(sub(p, a), sub(p, b)) <= 0
