# -*- coding: utf-8 -*-
import pytest
import copy
import sys, os
sys.path.insert(0, os.path.dirname(__file__) + '/../')
from bingo.card import Card


class TestCard:
    def setup(self):
        self.c1 = Card()
        self.c2 = Card(list(range(1, 26)))

    def teardown(self):
        pass

    def test_generated_numbers_is_25(self):
        assert len(self.c1.numbers) == 25

    def test_punched_number_is_zero(self):
        before_punched = copy.deepcopy(self.c2.numbers)
        self.c2.punch(1)
        assert before_punched != self.c2.numbers
        assert self.c2.numbers[0] == 0

    def test_misspunch_doesnt_change_numbers(self):
        before_punched = copy.deepcopy(self.c2.numbers)
        self.c2.punch(26)
        assert before_punched == self.c2.numbers

    def test_aa(self):
        """Expected output
          1  2  3  4  5
          6  7  8  9 10
         11 12  _ 14 15
         16 17 18 19 20
         21 22 23 24 25
        """
        print('')
        print(self.c2.aa)
        assert True is True

    def test_bingo(self):
        self.c2.punch(1)
        assert self.c2.is_bingo() is False

        self.c2.punch(2)
        assert self.c2.is_bingo() is False

        self.c2.punch(3)
        assert self.c2.is_bingo() is False

        self.c2.punch(4)
        assert self.c2.is_bingo() is False

        self.c2.punch(5)
        assert self.c2.is_bingo() is True
