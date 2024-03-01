def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """calculate the BMI for each person in the list"""
    bmi = []
    for h, w in zip(height, weight):
        bmi.append(w / (h**2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    pass
