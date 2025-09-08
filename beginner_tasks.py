# Beginner Python Tasks

A collection of beginner-level Python tasks with solutions.  

---

# Beginner Python Tasks Collection

def square_digits(n):
    """
    Given an integer, square every digit and concatenate them.
    Example: 9119 -> 811181
    """
    return int("".join(str(int(d) ** 2) for d in str(n)))


def descending_order(n):
    """
    Given a non-negative integer, return its digits in descending order.
    Example: 42145 -> 54421
    """
    return int("".join(sorted(str(n), reverse=True)))
