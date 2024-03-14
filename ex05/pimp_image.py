import numpy as np
from PIL import Image
from load_image import ft_load


def create_image(array: np.array, name: str) -> np.array:
    img = Image.fromarray(array)
    img.show()
    img.save(name + ".jpeg")
    return array


def ft_invert(array) -> np.array:
    """invert color"""
    print("Inverts the color of the image received.")
    return create_image(255 - array, 'invert')


def ft_red(array) -> np.array:
    """red color"""
    print("red the color of the image received.")
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    return create_image(array, 'red')


def ft_green(array) -> np.array:
    """green color"""
    print("green the color of the image received.")
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    return create_image(array, 'green')


def ft_blue(array) -> np.array:
    """blue color"""
    print("blue the color of the image received.")
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return create_image(array, 'blue')


def ft_gray(array) -> np.array:
    """gray color"""
    print("gray the color of the image received.")
    gray_channel = \
        (array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3)
    array[:, :, 0] = gray_channel
    array[:, :, 1] = gray_channel
    array[:, :, 2] = gray_channel
    return create_image(array, 'gray')


if __name__ == "__main__":
    ft_invert(ft_load("./landscape.jpeg"))
    ft_red(ft_load("./landscape.jpeg"))
    ft_green(ft_load("./landscape.jpeg"))
    ft_blue(ft_load("./landscape.jpeg"))
    ft_gray(ft_load("./landscape.jpeg"))
