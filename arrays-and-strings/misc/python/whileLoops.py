"""
Factorial Using While Loop

PATTERN: Basic Iteration - Accumulator Pattern
- Initialize result to identity value (1 for multiplication)
- Iterate while condition holds
- Accumulate result with each iteration

TIME COMPLEXITY: O(n) - n iterations for factorial of n
SPACE COMPLEXITY: O(1) - only storing result

WHY THIS WORKS:
- Factorial: n! = n × (n-1) × (n-2) × ... × 2 × 1
- We start with 1 and multiply by decreasing values
- When n reaches 1 or 0, we're done (base case: 0! = 1! = 1)
"""


def factorial(n: int) -> int:
    """
    Calculate factorial of n using a while loop.

    n! = n × (n-1) × (n-2) × ... × 2 × 1
    0! = 1 (by definition)

    Args:
        n: Non-negative integer

    Returns:
        n factorial

    Visual:
        n = 5

        result = 1
        n = 5: result = 1 * 5 = 5, n = 4
        n = 4: result = 5 * 4 = 20, n = 3
        n = 3: result = 20 * 3 = 60, n = 2
        n = 2: result = 60 * 2 = 120, n = 1
        n = 1: loop ends (n > 1 is False)

        Return: 120
    """
    result = 1

    while n > 1:
        result *= n
        n -= 1

    return result


def factorial_recursive(n: int) -> int:
    """
    Factorial using recursion.

    TIME: O(n), SPACE: O(n) for call stack

    Visual:
        factorial(5)
        = 5 * factorial(4)
        = 5 * 4 * factorial(3)
        = 5 * 4 * 3 * factorial(2)
        = 5 * 4 * 3 * 2 * factorial(1)
        = 5 * 4 * 3 * 2 * 1
        = 120
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_for_loop(n: int) -> int:
    """
    Factorial using for loop (most Pythonic).

    Uses range to iterate from 2 to n.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_math(n: int) -> int:
    """
    Factorial using math library.

    Most efficient for large numbers.
    """
    from math import factorial as math_factorial
    return math_factorial(n)


# Test cases
if __name__ == "__main__":
    # Basic examples
    print(f"0! = {factorial(0)}")   # 1
    print(f"1! = {factorial(1)}")   # 1
    print(f"4! = {factorial(4)}")   # 24
    print(f"5! = {factorial(5)}")   # 120
    print(f"10! = {factorial(10)}") # 3628800

    # Compare approaches
    print(f"\nRecursive 5! = {factorial_recursive(5)}")  # 120
    print(f"For loop 5! = {factorial_for_loop(5)}")     # 120
    print(f"Math lib 5! = {factorial_math(5)}")         # 120

    """
    ACCUMULATOR PATTERN:

    Initialize accumulator to identity value:
    - Addition: start with 0 (a + 0 = a)
    - Multiplication: start with 1 (a * 1 = a)
    - String concatenation: start with "" ("" + s = s)
    - List building: start with [] ([] + [x] = [x])

    Template:
        accumulator = identity_value
        while/for condition:
            accumulator = accumulator OP current_value
        return accumulator

    WHILE vs FOR LOOP:

    While loop:
    - When number of iterations unknown beforehand
    - When need explicit control over iteration variable
    - When loop condition isn't just "iterate over sequence"

    For loop:
    - When iterating over a known sequence/range
    - More Pythonic for counting loops
    - Less error-prone (no forgetting to increment)

    RECURSION vs ITERATION:

    Recursion:
    - More elegant for naturally recursive definitions
    - Risk of stack overflow for large inputs
    - Can be optimized with memoization/tail recursion

    Iteration:
    - More memory efficient (no call stack)
    - Often faster in practice
    - Better for simple accumulation patterns

    RELATED PATTERNS:
    - Sum of array elements (accumulator with +)
    - Product of array (accumulator with *)
    - String building (accumulator with concatenation)
    - Finding max/min (accumulator with comparison)
    """
