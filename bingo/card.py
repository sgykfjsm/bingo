# -*- coding: utf-8 -*-
from random import SystemRandom


class Card(object):
    """Card Class.

    attributes:
        numbers: the numbers printed on card
        > 一番左の列は1-15の中から5個選ばれている。
        > 同様に、左から2列目は16-30、中央列は31-45、右から2列目は46-60、
        > 一番右の列は61-75から5個ずつ（中央列のみフリースポットがあるので4個）
        > 選ばれている[2]。各列を「B・I・N・G・O」の5文字に対応させ、
        > 番号を選ぶ際に「Bの5」「Gの58」のようなコールをされることもある。
        from https://ja.wikipedia.org/wiki/%E3%83%93%E3%83%B3%E3%82%B4

    >>> Card(list(range(1, 10)))
    Traceback (most recent call last):
      ...
    ValueError: if argument numbers is not None, it should be numeric list and have just 25 numric letters
    >>> c = Card()
    >>> len(c.numbers)
    25
    >>> c = Card(list(range(1, 26)))
    >>> print(c.aa)
      1  2  3  4  5
      6  7  8  9 10
     11 12  _ 14 15
     16 17 18 19 20
     21 22 23 24 25
    >>> c.punch(11)
    >>> print(c.aa)
      1  2  3  4  5
      6  7  8  9 10
      _ 12  _ 14 15
     16 17 18 19 20
     21 22 23 24 25
    >>> c.is_bingo()
    False
    >>> c.punch(26)
    >>> print(c.aa)  # same as previous
      1  2  3  4  5
      6  7  8  9 10
      _ 12  _ 14 15
     16 17 18 19 20
     21 22 23 24 25
    >>> c.is_bingo()
    False
    >>> c.punch(12)
    >>> c.is_bingo()
    False
    >>> c.punch(14)
    >>> c.is_bingo()
    False
    >>> c.punch(15)
    >>> c.is_bingo()
    True
    >>> print(c.aa)
      1  2  3  4  5
      6  7  8  9 10
      _  _  _  _  _
     16 17 18 19 20
     21 22 23 24 25
    """
    def __init__(self, numbers=None):
        if numbers is not None:
            if len(numbers) != 25:
                msg = 'if argument numbers is not None, '
                msg += 'it should be numeric list '
                msg += 'and have just 25 numric letters'
                raise ValueError(msg)
            else:
                numbers[12] = 0  # free spot
        self.numbers = self.__generate() if numbers is None else numbers

    def __generate(self):
        random = SystemRandom()
        b, i, n, g, o = \
            [random.sample(list(range(x, (x * 15) + 1)), 5) for x in range(1, 6)]
        result = []
        for x in range(1, 26):
            if x == 13:  # free spot
                result.append(0)  # zero means 'opened'
                continue
            y = x % 5
            if y == 1:
                result.append(b.pop())
            elif y == 2:
                result.append(i.pop())
            elif y == 3:
                result.append(n.pop())
            elif y == 4:
                result.append(g.pop())
            elif y == 0:
                result.append(o.pop())
        return result

    def punch(self, number):
        if number in self.numbers:
            self.numbers[self.numbers.index(number)] = 0

    def is_bingo(self):
        if self.numbers.count(0) < 5:
            return False

        for x in range(0, 5):
            # yoko and tate
            if sum(self.numbers[x * 5:(x * 5) + 5]) == 0 \
                    or sum(self.numbers[x:x + 21:5]) == 0:

                return True

        # naname
        if sum(self.numbers[0:25:6]) == 0 or sum(self.numbers[4:21:4]) == 0:
            return True

        return False

    @property
    def aa(self):
        result = ''
        for i in range(0, 25):
            j = str(self.numbers[i]) if self.numbers[i] != 0 else '_'
            result += '{:>3}'.format(j)
            if (i + 1) % 5 == 0 and i != 24:
                result += '\n'
        return result
