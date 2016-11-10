# -*- coding: utf-8 -*-
import random


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
    """
    def __init__(self):
        self.numbers = self.__generate()

    def __generate(self):
        b = range(1, 16)
        i = range(16, 31)
        n = range(31, 46)
        g = range(46, 61)
        o = range(61, 76)
        random.shuffle(b)
        random.shuffle(i)
        random.shuffle(n)
        random.shuffle(g)
        random.shuffle(o)
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

        for x in range(0, 5):  # yoko
            if sum(self.numbers[x * 5:(x * 5) + 5]) == 0:
                return True

        for x in range(0, 5):  # tate
            if self.numbers[x] + self.numbers[x + 5] \
                    + self.numbers[x + 10] + self.numbers[x + 15] \
                    + self.numbers[x + 20] == 0:
                return True

        # naname
        if self.numbers[0] + self.numbers[6] \
                + self.numbers[12] + self.numbers[18] \
                + self.numbers[24] == 0 \
                or \
                self.numbers[4] + self.numbers[8] \
                + self.numbers[12] + self.numbers[16] \
                + self.numbers[20] == 0:
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


# TODO: Remove below later
if __name__ == '__main__':
    c = Card()
    print(c.aa)
    c.punch(10)
    print('')
    print(c.aa)
