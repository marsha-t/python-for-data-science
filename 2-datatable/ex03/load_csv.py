import pandas as pd


def validate_path(path: str) -> None:
    """
    Validate file path to CSV dataset

    Args:
        path (str):
            file path to CSV dataset

    Raises:
        TypeError:
            If file path is not a string
        ValueError:
            If file is not .csv
    """
    if not isinstance(path, str):
        raise TypeError("File path should be a string")
    if not path.lower().endswith(".csv"):
        raise ValueError("Only CSV formats allowed ")


def load(path: str) -> pd.DataFrame:
    """
    Load CSV dataset and print its dimensions

    Args:
        path (str):
            file path to CSV dataset

    Returns:
        pd.DataFrame | None:
            Loaded dataset (as pandas DataFrame) or None if error occurs

    Notes:
        Errors are printed
    """
    try:
        validate_path(path)
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
