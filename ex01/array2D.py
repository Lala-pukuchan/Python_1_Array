import numpy as np


def slice_me(family, start, end):
    """provide shape and trancate version of a 2D array"""
    try:
        assert isinstance(family, list), "family is not a list"
        for i in range(len(family)):
            assert isinstance(family[i], list), "family is not a 2D list"
            assert len(family[i]) == len(family[0]), "family is not a 2D list"
        arr = np.array(family)
        print(arr)

    except Exception as e:
        print(e)
        return None
