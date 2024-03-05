def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """calculate the BMI for each person in the list"""
    try:
        assert isinstance(height, list) and \
            isinstance(weight, list), "The input must be a list"
        assert len(height) == len(weight), "The list length must be the same"
        assert all(isinstance(h, (int, float)) for h in height) and \
            all(isinstance(w, (int, float)) for w in weight), \
            "The input must be a list of int or float"
        bmi = []
        for h, w in zip(height, weight):
            bmi.append(w / (h**2))
    except AssertionError as e:
        print("AssertionError:", e)
        return []
    except ZeroDivisionError:
        print("ZeroDivisionError: height cannot be 0")
        return []
    return bmi


def apply_limit(
    bmi: list[int | float],
    limit: int
) -> list[bool]:
    """apply a limit to the bmi"""
    try:
        assert isinstance(bmi, list) and isinstance(limit, int), \
            "The input must be a list and an int"
        assert all(isinstance(b, (int, float)) for b in bmi), \
            "The input must be a list of int or float"
    except AssertionError as e:
        print("AssertionError:", e)
        return []
    return [True if b >= limit else False for b in bmi]
