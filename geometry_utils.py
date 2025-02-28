import math as mt


def get_diag(a: float, b: float, c: float) -> float:
    return round(mt.sqrt(a**2 + b**2 + c**2), 2)


def get_volume(a: float, b: float, c: float) -> float:
    return a * b * c


def get_surface(a: float, b: float, c: float) -> float:
    return 2 * (a * b + a * c + b * c)


def get_alpha(a: float, b: float, c: float) -> float:
    return round(mt.acos(a / mt.sqrt(a**2 + b**2 + c**2)), 2)


def get_beta(a: float, b: float, c: float) -> float:
    return round(mt.acos(b / mt.sqrt(a**2 + b**2 + c**2)), 2)


def get_gamma(a: float, b: float, c: float) -> float:
    return round(mt.acos(c / mt.sqrt(a**2 + b**2 + c**2)), 2)


def get_sphr_radius(a: float, b: float, c: float) -> float:
    return round(mt.sqrt(a**2 + b**2 + c**2) / 2, 2)


def get_sphr_volume(a: float, b: float, c: float) -> float:
    return round(4 / 3 * mt.pi * (mt.sqrt(a**2 + b**2 + c**2) / 2) ** 3, 2)
