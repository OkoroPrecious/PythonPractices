import doctest


def add(a, b):
    """
    >>> add(3, 5)
    8
    """
    return a + b


if __name__ == '_main_':
    doctest.testmod()

# to run on terminal type - python -m doctest documentTest.py -v
