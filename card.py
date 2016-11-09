# -*- coding: utf-8 -*-
import uuid
import random


class Card(object):
    """Card Class.

    attributes:
        id: card id
        numbers: the numbers printed on card
        > $B0lHV:8$NNs$O(B1-15$B$NCf$+$i(B5$B8DA*$P$l$F$$$k!#(B
        > $BF1MM$K!":8$+$i(B2$BNsL\$O(B16-30$B!"Cf1{Ns$O(B31-45$B!"1&$+$i(B2$BNsL\$O(B46-60$B!"(B
        > $B0lHV1&$NNs$O(B61-75$B$+$i(B5$B8D$:$D!JCf1{Ns$N$_%U%j!<%9%]%C%H$,$"$k$N$G(B4$B8D!K(B
        > $BA*$P$l$F$$$k(B[2]$B!#3FNs$r!V(BB$B!&(BI$B!&(BN$B!&(BG$B!&(BO$B!W$N(B5$BJ8;z$KBP1~$5$;!"(B
        > $BHV9f$rA*$V:]$K!V(BB$B$N(B5$B!W!V(BG$B$N(B58$B!W$N$h$&$J%3!<%k$r$5$l$k$3$H$b$"$k!#(B
        from https://ja.wikipedia.org/wiki/%E3%83%93%E3%83%B3%E3%82%B4
    """
    def __init__(self):
        self.id = uuid.uuid4().hex
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
        for x in range(1, 26):  # col
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
            b = self.numbers[x]
            i = self.numbers[x + 5]
            n = self.numbers[x + 10]
            g = self.numbers[x + 15]
            o = self.numbers[x + 20]
            if b + i + n + g + o == 0:
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

    def aa(self):
        result = ''
        for i in range(0, 25):
            j = str(self.numbers[i]) if self.numbers[i] != 0 else '_'
            result += '{:>3}'.format(j)
            if (i + 1) % 5 == 0 and i != 24:
                result += '\n'
        return result


if __name__ == '__main__':
    c = Card()
    print(c.aa())
    c.punch(10)
    print('')
    print(c.aa())
