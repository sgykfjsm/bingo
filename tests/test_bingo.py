# -*- coding: utf-8 -*-
import pytest
import copy
import sys, os
sys.path.insert(0, os.path.dirname(__file__) + '/../')
from bingo.bingo import Bingo
from bingo.cage import CageEmptyError


class TestBingo:
    def setup(self):
        self.players = ['a', 'b', 'c']

    def test_bingo(self):
        b = Bingo(self.players)

        for _ in range(1, 76):
            number = b.draw()
            assert 0 < number < 76

        assert len(b.winners) == len(self.players)

        with pytest.raises(CageEmptyError):
            b.draw()
