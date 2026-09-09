import numpy as np
import matplotlib.pyplot as plt


def validate_image(img_array: np.ndarray) -> np.ndarray:
    """
    Validates RGB image array

    Args:
        img_array (np.ndarray):
            RGB image represented as NumPy array

    Returns:
        np.ndarray:
            Original image array if valid
            Empty array if validation fails

    Notes:
        Prints error message if validation fails
    """
    if not isinstance(img_array, np.ndarray):
        print("TypeError: img_array must be a NumPy array")
        return np.array([])
    if img_array.ndim != 3 or img_array.shape[2] != 3:
        print("ValueError: image must have 3 RGB channels")
        return np.array([])

    return img_array


def display_image(img_array: np.ndarray, cmap=None) -> None:
    """
    Display image using matplotlib

    Args:
        img_array (np.ndarray):
            image represented as NumPy array
        cmap (str | None = None):
            colour map
    """
    plt.imshow(img_array, cmap=cmap)
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts colours of image received

    Args:
        array (np.ndarray):
            RGB image represented as NumPy array

    Returns:
        np.ndarray:
            Inverted image array
            Empty array if validation fails

    Notes:
        Displays transformed image
    """
    array = validate_image(array)
    if array.size == 0:
        return array
    inverted = 255 - array
    display_image(inverted)
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Retains only red channel of RGB image received

    Args:
        array (np.ndarray):
            RGB image represented as NumPy array

    Returns:
        np.ndarray:
            Red-only image array
            Empty array if validation fails

    Notes:
        Displays transformed image
    """
    array = validate_image(array)
    if array.size == 0:
        return array
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    display_image(red)
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Retain only green channel of RGB image received

    Args:
        array (np.ndarray):
            RGB image represented as NumPy array

    Returns:
        np.ndarray:
            Green-only image array
            Empty array if validation fails

    Notes:
        Displays transformed image
    """
    array = validate_image(array)
    if array.size == 0:
        return array
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    display_image(green)
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Retain only blue channel of RGB image received

    Args:
        array (np.ndarray):
            RGB image represented as NumPy array

    Returns:
        np.ndarray:
            Blue-only image array
            Empty array if validation fails

    Notes:
        Displays transformed image
    """
    array = validate_image(array)
    if array.size == 0:
        return array
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    display_image(blue)
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Generate greyscale version of RGB image received

    Args:
        array (np.ndarray):
            RGB image represented as NumPy array

    Returns:
        np.ndarray:
            Greyscale image array
            Empty array if validation fails

    Notes:
        Displays transformed image
    """
    array = validate_image(array)
    if array.size == 0:
        return array
    gray = (np.sum(array, axis=2, keepdims=True) / 3).astype(np.uint8)
    gray = np.repeat(gray, 3, axis=2)
    display_image(gray)
    return gray
