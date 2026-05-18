def ft_filter(function, iterable):
    """
    Filter elements from an iterable based on given function

    Args:
        function (callable | None):
            function used to test each element
            if None, falsy values are removed
        iterable (iterable):
            collection of elements to filter

    Returns:
        list:
            list containing elements where
                - function(element) is True or
                - element is Truthy (if function is None)

    """
    if function is None:
        return [x for x in iterable if x]
    return [x for x in iterable if function(x)]
