from run import task1
import pytest
import os

os.chdir(os.path.dirname(__file__))


#from run import task1


def test_task1():
    powerConsumtion = task1("example.txt")
    assert powerConsumtion == 198
