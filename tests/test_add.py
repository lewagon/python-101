from nose.tools import eq_
from add import add_

def test_numbers_0_0_0():
    eq_(add_(0, 0), 0)

def test_numbers_1_2():
    eq_(add_(1, 2), 3)
