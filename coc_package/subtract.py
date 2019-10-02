def subtract(a, b):
    """
    A function that subtracts 2nd integer from 1st

    :param a: (int) The first integer
    :param b: (int) The second integer
    :return: (int) The difference of a and b
    :raises: AttributeError, if a and b are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise AttributeError("This function only accepts integer arguments")
    return a - b
