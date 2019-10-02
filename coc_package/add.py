def add(a, b):
    """
    A function that adds two integers

    :param a: (int) The first integer
    :param b: (int) The second integer
    :return: (int) The sum of a and b
    :raises: AttributeError, if a and b are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise AttributeError("This function only accepts integer arguments")
    return a + b
