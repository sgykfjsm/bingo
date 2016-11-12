# -*- coding: utf-8 -*-
import random


class Cage(object):
    """
    >>> c = Cage()
    >>> len(c.numbers)
    75
    >>> i = c.pop()
    >>> len(c.numbers)
    74
    >>> i in c.numbers
    False
    >>> i in c.out
    True

    # >>> _ = [c.pop() for _ in range(1, 75)]
    # >>> c.pop()
    # Traceback (most recent call last):
    #   ...
    ### Python2
    # CageEmptyError: The cage has been already empty.
    ### Python3
    # bingo.cage.CageEmptyError: The cage has been already empty.
    """
    numbers = list(range(1, 76))

    def __init__(self):
        self.out = []

    def pop(self):
        if len(self.numbers) == 0:
            raise CageEmptyError('The cage has been already empty.')

        i = random.sample(self.numbers, 1)[0]
        self.out.append(i)
        self.numbers.remove(i)
        return i


class CageEmptyError(Exception):
    """Raised when a cage has no number in its slot."""
    pass
