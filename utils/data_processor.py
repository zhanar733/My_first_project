from utils.geometry_utils import (
    get_diag,
    get_volume,
    get_surface,
    get_alpha,
    get_beta,
    get_gamma,
    get_sphr_radius,
    get_sphr_volume,
)


def calculate_characteristics(parallelepipeds: dict) -> dict:
    characteristics = {}
    for name, values in parallelepipeds.items():
        a = int(values["a"])
        b = int(values["b"])
        c = int(values["c"])
        characteristics[name] = {
            "diag": str(get_diag(a, b, c)),
            "volume": str(get_volume(a, b, c)),
            "surface_area": str(get_surface(a, b, c)),
            "alpha": str(get_alpha(a, b, c)),
            "beta": str(get_beta(a, b, c)),
            "gamma": str(get_gamma(a, b, c)),
            "radius_described_sphere": str(get_sphr_radius(a, b, c)),
            "volume_described_sphere": str(get_sphr_volume(a, b, c)),
        }
    return characteristics
