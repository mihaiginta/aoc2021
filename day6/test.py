import pytest
from run import task1


def test_task1():
    powerConsumtion = task1("example.txt")
    assert powerConsumtion == 198
