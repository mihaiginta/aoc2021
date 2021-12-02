import pytest

from run import task1

#from run import task1

def test_task1():
    position = task1("example1.txt")
    assert position==150
