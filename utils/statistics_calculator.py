def calculate_statistics(characteristics: dict) -> dict:
    statistics = {}
    len_ = len(characteristics)
    char_values = characteristics.values()

    avg_diag = sum(float(k["diag"]) for k in char_values) / len_
    avg_volume = sum(float(k["volume"]) for k in char_values) / len_
    avg_surface = sum(float(k["surface_area"]) for k in char_values) / len_
    avg_alpha = sum(float(k["alpha"]) for k in char_values) / len_
    avg_beta = sum(float(k["beta"]) for k in char_values) / len_
    avg_gamma = sum(float(k["gamma"]) for k in char_values) / len_
    avg_radius_described_sph = (
        sum(float(k["radius_described_sphere"]) for k in char_values) / len_
    )
    avg_volume_described_sph = (
        sum(float(k["volume_described_sphere"]) for k in char_values) / len_
    )

    statistics = {
        "avg_diag": str(round(avg_diag, 2)),
        "avg_volume": str(round(avg_volume)),
        "avg_surface_area": str(round(avg_surface, 2)),
        "avg_alpha": str(round(avg_alpha * (180 / 3.14), 2)),
        "avg_beta": str(round(avg_beta * (180 / 3.14), 2)),
        "avg_gamma": str(round(avg_gamma * (180 / 3.14), 2)),
        "avg_radius_described_sphere": str(round(avg_radius_described_sph, 2)),
        "avg_volume_described_sphere": str(round(avg_volume_described_sph, 2)),
    }
    return statistics
