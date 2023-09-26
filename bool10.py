from math import *
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    x=sqrt(a)
    y=x*x==a
    return y
print(main(4))