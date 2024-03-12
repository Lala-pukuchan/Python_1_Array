import numpy as np
from PIL import Image
from load_image import ft_load


def zoom(array: np.array):
    """zoom picture in"""
    try:
        sliced_array = array[200:600, 200:600, 0:1]
        new_array = np.squeeze(sliced_array, axis=2)
        print("The New shape of image is:", new_array.shape)
        img = Image.fromarray(new_array)
        img.show()
        img.save("zoomed_image.jpeg")
        return new_array
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


if __name__ == "__main__":
    print(ft_load("./animal.jpeg"))
    print(zoom(ft_load("./animal.jpeg")))
