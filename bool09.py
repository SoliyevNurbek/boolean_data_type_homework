from math import *
def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    x=a>0 and a/1==round(a)
    return x
print(main(4.005))