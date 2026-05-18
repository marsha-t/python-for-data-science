import os


def ft_tqdm(lst: range) -> None:
    """
    Display progress bar while iterating over iterable.

    Args:
        lst (range):
            iterable to wrap and track progress for

    Yields:
        item from iterable
    """

    length = len(lst)
    terminal_width = os.get_terminal_size().columns
    bar_width = terminal_width - 41

    for i, item in enumerate(lst, 1):
        percent = round((i / length) * 100)
        filled_width = round((i / length) * bar_width)
        bar = f"{'█' * filled_width:<{bar_width}}"  # Left aligned bar
        print(f"\r{percent:>3}%|{bar}|{i}/{length}", end="", flush=True)
        yield item
