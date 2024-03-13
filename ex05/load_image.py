import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """Load an image from a file and return it as a numpy array."""
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print("The shape of image is:", img_array.shape)
        return img_array
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


if __name__ == "__main__":
    img = ft_load("./landscape.jpeg")
