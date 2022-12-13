# 3. (1.0 points) Oh, Camel!

# Definition: A camel sequence is an integer in which each digit is either strictly less than or strictly greater
# than both of its adjacent digits. 
# Write a function is_camel_sequence that takes in a nonnegative integer n
# and returns whether n is a camel sequence.
# Note: Any single digit integer is a valid camel sequence.
# Restrictions: You may not use int, str, [ or ] in your solution.

def is_camel_sequence(n):
    """
    >>> is_camel_sequence(15263) # 1 < 5, 5 > 2, 2 < 6, 6 > 3
    True
    >>> is_camel_sequence(98989)
    True
    >>> is_camel_sequence(123) # 1 < 2, but 2 is not greater than 3.
    False
    >>> is_camel_sequence(4114) # 1 is not strictly less than 1
    False
    >>> is_camel_sequence(1)
    True
    >>> is_camel_sequence(12)
    True
    >>> is_camel_sequence(11)
    False
    """
    def helper(n, incr):
        if n < 10:
            return True
        elif incr:
            return n % 10 < n // 10 % 10 and helper(n // 10, not incr)
        else:
            return n % 10 > n // 10 % 10 and helper(n // 10, not incr)
    return n < 10 or helper(n, n // 10 % 10 > n % 10)