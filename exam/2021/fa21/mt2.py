
s = [3, 4]
s.append([s])
s[2].extend(s[1:])
s[2] = [s[2].pop()]

# 2. (11.0 points) Doctor Chang

# (a) (6.0 points)
# Implement change, a function that takes an integer n and a list of positive integers coins. It returns
# whether there is a subset of the values in coins that sums to n. As a side effect, change modifies coins.

def change(n, coins):
    """Return whether a subset of coins adds up to n.
    >>> change(10, [2, 7, 1, 8, 2]) # e.g., 2 + 8
    True
    >>> change(20, [2, 7, 1, 8, 2]) # e.g., 2 + 7 + 1 + 8 + 2
    True
    >>> change(6, [2, 7, 1, 8, 2]) # Impossible; only two 2's in coins
    False
    """
    if n == 0:
        return True
    elif n < 0 or len(coins) == 0:
        return False
    coin = coins.pop() # remove the end of coins and name it "coin"
    return change(n, list(coins)) or change(n - coin, list(coins))

# (b) (5.0 points)
# Implement amounts, which takes a list of positive integers coins. It returns a sorted list of all unique
# non-negative integers n for which change(n, coins) returns True. You may not call change.
def amounts(coins):
    """List all unique n such that change(n, coins) returns True (in sorted order).
    >>> amounts([2, 5, 3])
    [0, 2, 3, 5, 7, 8, 10]
    >>> amounts([2, 7, 1, 8, 2])
    [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    """
    if not coins:
        return [0]
    coin = coins[0]
    rest = amounts(coins[1:])
    return sorted(rest + [k + coin for k in rest if k + coin not in rest])



# 3. (13.0 points) Shang-Chi

# (a) (6.0 points)
# Implement the Valet and Garage classes.
# A Valet instance has two instance attributes: their total tips and the garage where they work (a Garage
# instance).
# • The park method takes a string car and parks it in the Garage where they work.
# • The wash method takes a string car that has been parked in their garage and a number tip. The
# Valet who washed the car and the Valet who most recently parked the car split the tip.

# The Garage constructor takes a list of the Valets who work in that Garage. Assume that park and wash
# are only invoked on a Valet that already has a Garage.
class Valet:
    """A valet is tipped after they wash a car,
    or after one of their parked cars is washed.
    >>> shaun = Valet()
    >>> katy = Valet()
    >>> g = Garage([shaun, katy])
    >>> shaun.park('Benz')
    >>> katy.park('BMW')
    >>> shaun.wash('Benz', 1) # $1.0 to Shaun
    >>> katy.wash('Benz', 2) # $1.0 to Katy, $1.0 to Shaun
    >>> shaun.park('Rolls')
    >>> katy.park('Rolls')
    >>> katy.wash('BMW', 2) # $2.0 to Katy
    >>> shaun.wash('Rolls', 2) # $1.0 to Shaun, $1.0 to Katy
    >>> [shaun.tips, katy.tips]
    [3.0, 4.0]
    """
    def __init__(self):
            self.tips = 0       # their total tips
            self.garage = None  # the Garage where they work.

    def park(self, car):
            if self.garage:
                self.garage.cars[car] = self

    def wash(self, car, tip):
            self.tips += tip / 2
            self.garage.cars[car].tips += tip / 2

class Garage:
    """A garage holds cars parked by the valets who work there."""
    def __init__(self, valets):
        self.cars = {}
        for valet in valets:
            valet.garage = self

# (b) (2.0 points)
# Definition.
# An infinite iterator t is one for which next(t) can be called any number of times and always returns a value.
# Implement ring, a generator function that takes a non-empty list s. It returns an infinite generator that
# repeatedly yields the values of s in the order they appear in s.
def ring(s):
    """Yield all values of non-empty s in order, repeatedly.
    >>> t = ring([2, 5, 3])
    >>> [next(t), next(t), next(t), next(t), next(t), next(t), next(t)]
    [2, 5, 3, 2, 5, 3, 2]
    """
    while True:
        yield from s


# (c) (5.0 points)
# Implement fork, a function that takes an infinite iterator t. 
# It returns two infinite iterators that each iterate over the contents of t.
def fork(t):
    """Return two iterators with the same contents as infinite iterator t.
    >>> a, b = fork(ring([1, 2, 3]))
    >>> [next(a), [next(b), next(b), next(b)], next(a), [next(b), next(b), next(b)], next(a)]
    [1, [1, 2, 3], 2, [1, 2, 3], 3]
    """
    s = []
    def copy():
        i = 0
        while True:
            if len(s) == i:
                s.append(next(t))
            yield s[i]
            i += 1
    return copy(),copy()

# 4. (10.0 points) Thanos
# Hint: you may call built-in sequence functions: sum, max, min, all, any, map, filter, zip, and reversed.
# (a) (4.0 points)
# Implement snap, which takes a one-argument function f, a one-argument function g, and a sequence s. It
# returns a list of (x, f(x)) pairs (two-element tuples) for all x in s for which g(f(x)) is a true value. The
# implementation of snap only calls f once per element of s; never twice.
# Important: For full credit, your implementation may only call f once on each element of s.
def snap(f, g, s):
    """Return a list of (x, f(x)) pairs for each x in s such that g(f(x)) is a true value.
    >>> snap(lambda x: x * x, lambda x: x < 10, range(5))
    [(0, 0), (1, 1), (2, 4), (3, 9)]
    >>> snap(lambda x: x * x, lambda x: x > 10, range(5))
    [(4, 16)]
    >>> snap(lambda x: x * x, lambda x: x and x - 9, range(5))
    [(1, 1), (2, 4), (4, 16)]
    """
    return [(x, y) for x,y in zip(s,map(f,s)) if g(y)]


# (b) (4.0 points)
# Implement max_diff, which takes a non-empty sequence s and a one-argument function f. 
# It returns a pair of elements (v, w) in s for which f(v) - f(w) is largest. v and w may be the same or different
# elements of s. Also, describe the order of growth of the run time of max_diff.
def max_diff(s, f):
    """Return two elements (v, w) of s for which f(v) - f(w) is largest.
    >>> max_diff(range(-7, 4), lambda x: x * x) # (-7 * -7) - (0 * 0) = 49
    (-7, 0)
    >>> max_diff(['what', 'a', 'great', 'film'], len) # len('great') - len('a')
    ('great', 'a')
    """
    assert s, 's cannot be empty'
    v, w = None, None
    for x in s:
        for y in s:
            if v is None or f(x) - f(y) > f(v) - f(w):
                v,w = x,y
    return v, w

# Quadratic, Θ(n2)

# (c) (2.0 points)

# Implement max_diff_fast, which has the same signature and behavior as max_diff, but has a faster
# order of growth of its run time.

# Important. You may not use a list comprehension in your solution

def max_diff_fast(s, f):
    return max(s,key=f) , min(s,key=f)


# 5. (9.0 points) Groot

# Definition. 
# A twig is a tree that is not a leaf but whose branches are all leaves.
# The Tree and Link classes appear on your midterm 2 study guide. Assume they are defined.

# (a) (4.0 points)
# Implement twig, which takes a Tree instance t. It returns True if t is a twig and False otherwise.
def twig(t):
    """Return True if Tree t is a twig and False otherwise.
    >>> twig(Tree(1))
    False
    >>> twig(Tree(1, [Tree(2), Tree(3)]))
    True
    >>> twig(Tree(1, [Tree(2), Tree(3, [Tree(4)])]))
    False
    """
    return not t.is_leaf() and len([branch for branch in t.branches if t.is_leaf()]) == len(t.branches)

# (b) (5.0 points)
# Implement twigs, which takes a Tree instance t. It returns a linked list (either a Link instance or
# Link.empty) containing all of the labels of the twigs in t. Labels should be in the same order as they
# appear in repr(t).


def twigs(t):
    """Return a linked list of the labels of the twigs in t.
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(5, [Tree(6, [Tree(7), Tree(8)])])])
    >>> print(twigs(t))
    <3 6>
    >>> print(twigs(Tree(0, [t, t, t])))
    <3 6 3 6 3 6>
    >>> twigs(Tree(0)) is Link.empty
    True
    """
    def add_twigs(t, rest):
        if twig(t):
            return Link(t.label,rest)
        for b in reversed(t.branches):
            rest = add_twigs(b,rest)
        return rest
    return add_twigs(t, Link.empty)