from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its shape and pixels,
    and return it as NumPy array

    Args:
        path (str):
            path to image file

    Returns:
        np.ndarray:
            image converted into NumPy array

    Notes:
        Prints error message and returns empty array if loading fails
    """

    if not isinstance(path, str):
        print("TypeError: path must be a string")
        return np.array([])

    if not path.lower().endswith((".jpg", ".jpeg")):
        print("ValueError: Only JPG and JPEG formats are supported")
        return np.array([])

    try:
        with Image.open(path) as image:
            img_array = np.array(image)
            return img_array
    except FileNotFoundError:
        print(f"File not found: {path}")
        return np.array([])
    except UnidentifiedImageError:
        print(f"Cannot open image: {path}")
        return np.array([])
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return np.array([])
