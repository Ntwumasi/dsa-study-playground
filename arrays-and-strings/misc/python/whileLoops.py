def factorial(n):
    """
    Calculate the factorial of a number using a while loop.
    :param n: The number to calculate the factorial for.
    :return: The factorial of n.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print(factorial(4))  # Output: 120