# 1. (8.0 points) What Would Python Display?
# (a) (4.0 points)
# Assume the following code has been executed

def os(ki):
   t = -1  #  相当于JS中  let t = -1

i = 5
t = 7

while i > 3:
    t = i - 4 and i + 4
    os(i - 2)
    i, j = i - 1, i * 2
    s = i


# (b) (4.0 points)
# The function tik takes an argument tok and returns a function insta that takes an argument gram. The
# insta function prints tok and gram on the same line separated by a space and has no return statement.
# Its implementation has been omitted intentionally.

def tik(tok):
    """Returns a function that takes gram and prints tok and gram on a line.
    >>> tik(5)(6)
    5 6
    """
    def insta(gram):
        # The implementation of this function has been omitted.
        pass

    return insta

# i. (4.0 pt) What would the interactive Python interpreter display upon evaluating the expression:

tik(tik(5)(print(6)))(print(7))
# 6
# 5 None
# 7
# None None


# 2. (5.0 points) 31 Cal Olympians
olympics = 2020
held = 2021

def swim(held):
    ...
    def row(swim):
        swim = held
        return lambda swim: held
    return row(7)

hand = swim(3)
hand(held)


# 3. (27.0 points) All Hail the Stone

from operator import add, mul

def next_hail(k):
    """Return the next element in a hailstone sequence."""
    assert k > 1
    if k % 2 == 0:
        return k // 2
    else:
        return 3 * k + 1


# (a) (8.0 points)

# Implement hail_min, which takes a positive integer n and a one-argument function measure. It returns
# the element of the hailstone sequence starting with n for which calling measure on the element returns the
# smallest value.
# If more than one element of the sequence has the smallest measure value, return the earliest one.

def hail_min(n, measure):
    """Return the element k of the hailstone sequence starting with n for which
    measure(k) is smallest. In case of a tie, return the earliest element.
    >>> hail_min(5, lambda k: -k) # Among 5, 16, 8, 4, 2, 1; 16 is largest
    16
    >>> hail_min(8, lambda k: -k) # Among 8, 4, 2, 1; 8 is largest
    8
    >>> hail_min(3, lambda k: abs(k - 7)) # Among 3, 10, 5, 16, 8, 4, 2, 1; 8 is closest to 7
    8
    >>> hail_min(9, lambda k: abs(k - 7)) # Among 9, 28, 14, 7, 22, ...; 7 is closest to 7
    7
    >>> hail_min(8, lambda k: abs(k - 3)) # 4 and 2 are both close to 3, but 4 is earliest
    4
    """
    apple = n

    while n > 1:
        n = next_hail(n)
        if measure(n) < measure(apple):
            apple = n
    return apple


# (b) (6.0 points)
"""
    Definition: An accumulator function is a function that takes two integers and returns an integer. It can
    serve as the second argument to hail_tally below.
"""

def hail_tally(n, f):
    """Accumulate the elements of the hailstone sequence starting with n using
    accumulator function f.
    >>> hail_tally(3, add) # 3 + 10 + 5 + 16 + 8 + 4 + 2 + 1 = 49
    49
    >>> hail_tally(10, max) # Largest of 10, 5, 16, 8, 4, 2, 1
    16
    """
    total = 0
    while n > 1:
        total = f(total, n)
        n = next_hail(n)
    return f(total, 1)


def sum_some(select):
    """Return an accumulator function that sums all k for which select(k) is a true value.
    >>> def below_ten(k):
    ... return k < 10
    >>> sum_below_ten = sum_some(below_ten)
    >>> hail_tally(3, sum_below_ten) # [3] + 10 + [5] + 16 + [8] + [4] + [2] + [1]
    23
    """
    def f(total, k):
        if select(k):
            return add(total, k)
        return total
    return f


# (c) (5.0 points)
# Implement hail_odd_sum, a function that takes a positive integer n and returns the sum of all odd elements
# in the hailstone sequences starting with n.
# Important: Your solution must include sum_some.
# You may also call other functions defined previously in this question.

def hail_odd_sum(n):
    """Sum the odd elements of the hailstone sequence starting with n.
    >>> hail_odd_sum(3) # [3], 10, [5], 16, 8, 4, [1]; 3 + 5 + 1 = 9
    9
    >>> hail_odd_sum(34) # 34, [17], 52, 26, [13], 40, 20, 10, [5], ..., [1]
    36
    """
    return hail_tally(n, sum_some(lambda x : x % 2 == 1))

#(d) (8.0 points)
# Definition: To call a function f repeatedly on a sequence of values x, y, z means to use f in a nested call
# expression in which each element of the sequence is passed in as a single argument in order: f(x)(y)(z).

def hail(n):
    """Return a function that returns True if called repeatedly on the remaining
    elements of the hailstone sequence starting with n and False otherwise.
    >>> hail(3)(10)(5)(16)(8)(4)(2)(1)
    True
    >>> hail(3)(4) # The next element should have been 10.
    False
    >>> hail(3)(10)(5)(16)(8)(1) # The next element should have been 4.
    False
    """
    assert n > 1
    def check(k):
        if next_hail(n) == 1 and k == 1:
            return True
        if next_hail(n) != k:
            return False
        return hail(k)
    return check
