def add(a, b):
    """
    A function that adds two integers
    this is just to try git add and push
    :param a: (int) The first integer
    :param b: (int) The second integer
    :return: (int) The sum of a and b
    :raises: AttributeError, if a and b are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise AttributeError("This function only accepts integer arguments")
    return a + b
