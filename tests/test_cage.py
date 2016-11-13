# -*- coding: utf-8 -*-
import pytest
import copy
import sys, os
sys.path.insert(0, os.path.dirname(__file__) + '/../')
from bingo.cage import Cage, CageEmptyError


class TestCage:
    def setup(self):
        self.c = Cage()

    def teardown(self):
        pass

    def test_init(self):
        assert len(self.c.out) == 0
        assert len(self.c.numbers) == 75

    def test_pop(self):
        self.c.pop()
        assert len(self.c.out) == 1
        assert len(self.c.numbers) == 74
        assert self.c.out[0] not in self.c.numbers

    def test_too_many_pop(self):
        [self.c.pop() for _ in range(0, 75)]
        with pytest.raises(CageEmptyError):
            self.c.pop()
