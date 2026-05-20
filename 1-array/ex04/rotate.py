import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(
    img_array: np.ndarray,
    area: tuple[int, int, int, int]
) -> np.ndarray:
    """
    Zoom into an image array using the provided crop area.

    Args:
        img_array (np.ndarray):
            image represented as a NumPy array
        area (tuple[int, int, int, int]):
            crop area formatted as (y_start, y_end, x_start, x_end)

    Returns:
        np.ndarray:
            Cropped image array

    Notes:
        Prints error message and returns empty array if validation fails
    """

    if not isinstance(img_array, np.ndarray):
        print("TypeError: img_array must be a NumPy array")
        return np.array([])
    if img_array.ndim != 3 or img_array.shape[2] != 3:
        print("ValueError: image must have 3 RGB channels")
        return np.array([])
    if not isinstance(area, tuple):
        print("TypeError: area must be a tuple")
        return np.array([])
    if len(area) != 4:
        print("ValueError: area must contain 4 integers")
        return np.array([])
    if not all(isinstance(value, int) for value in area):
        print("TypeError: area values must be integers")
        return np.array([])

    y1, y2, x1, x2 = area

    if y2 <= y1 or x2 <= x1:
        print("ValueError: invalid crop boundaries")
        return np.array([])

    height, width = img_array.shape[:2]

    if (y1 < 0 or x1 < 0 or y2 > height or x2 > width):
        print("ValueError: crop area exceeds image dimensions")
        return np.array([])

    zoomed = img_array[y1:y2, x1:x2]
    gray = np.mean(zoomed, axis=2, keepdims=True).astype(np.uint8)

    return gray


def ft_transpose(
    img_array: np.ndarray,
) -> np.ndarray:
    """
    Rotate image array

    Args:
        img_array (np.ndarray):
            image represented as a NumPy array

    Returns:
        np.ndarray:
            Transposed image array

    Notes:
        Prints error message and returns empty array if validation fails
    """

    if not isinstance(img_array, np.ndarray):
        print("TypeError: img_array must be a NumPy array")
        return np.array([])
    if img_array.ndim != 3 or img_array.shape[2] != 1:
        print("ValueError: image must have shape (H, W, 1)")
        return np.array([])
    height, width = img_array.shape[:2]
    transposed = np.zeros((width, height), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            transposed[x, y] = img_array[y, x, 0]

    return transposed


def main():
    """
    Load image, rotate it, and display the result
    """

    animal = ft_load("animal.jpeg")
    if animal.size == 0:
        return

    zoomed = ft_zoom(animal, (100, 400, 500, 800))
    if zoomed.size == 0:
        return
    print(f"The shape of image is: {zoomed.shape}")
    print(zoomed)

    transposed = ft_transpose(zoomed)
    if transposed.size == 0:
        return

    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    plt.imshow(transposed.squeeze(), cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
