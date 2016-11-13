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

    @pytest.mark.parametrize("test_data, expected", [
        # yoko
        ([1], False),
        ([1, 2], False),
        ([1, 2, 3], False),
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 4, 5], True),
        ([11], False),
        ([11, 12], False),
        ([11, 12, 14], False),
        ([11, 12, 14, 15], True),  # 13 has been already opened because 13 is free spot.
        # tate
        ([1], False),
        ([1, 6], False),
        ([1, 6, 11], False),
        ([1, 6, 11, 16], False),
        ([1, 6, 11, 16, 21], True),
        ([3], False),
        ([3, 8], False),
        ([3, 8, 18], False),
        ([3, 8, 18, 23], True),  # 13 has been already opened because 13 is free spot.
        # naname
        ([1], False),
        ([1, 7], False),
        ([1, 7, 19], False),
        ([1, 7, 19, 25], True),  # 13 has been already opened because 13 is free spot.
        ([5], False),
        ([5, 9], False),
        ([5, 9, 17], False),
        ([5, 9, 17, 21], True),  # 13 has been already opened because 13 is free spot.
        # no bingo
        ([1], False),
        ([1, 3], False),
        ([1, 3, 5], False),
        ([1, 3, 5, 7], False),
        ([3, 3, 5, 7, 9], False),
        ([3], False),
        ([3, 9], False),
        ([3, 9, 27], False),
        ([3, 9, 27, 72], False),
        ([3, 9, 27, 72, 29], False),
    ])
    def test_bingo(self, test_data, expected):
        for x in test_data:
            self.c2.punch(x)
        print(self.c2.aa)
        assert self.c2.is_bingo() is expected
