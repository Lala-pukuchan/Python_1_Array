import numpy as np
from PIL import Image
from load_image import ft_load


def rotate(array: np.array):
    """rotate picture in"""
    try:
        sliced_array = array[200:600, 200:600, 0:1]
        sliced = np.squeeze(sliced_array, axis=2)
        print("The shape after Slice:", sliced)
        img = Image.fromarray(sliced)
        img.show()
        img.save("sliced_image.jpeg")
        rotated = np.zeros(shape=sliced.shape)
        len = sliced.shape[0]
        for x in range(sliced.shape[0]):
            for y in range(sliced.shape[1]):
                rotated[len - 1 - y, x] = sliced[x, y]
        print("The shape after Rotate:", rotated.astype(np.uint8))
        img = Image.fromarray(rotated.astype(np.uint8))
        img.show()
        img.save("rotated_image.jpeg")
        return array
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


if __name__ == "__main__":
    # print(ft_load("./animal.jpeg"))
    # print(rotate(ft_load("./animal.jpeg")))
    rotate(ft_load("./animal.jpeg"))
