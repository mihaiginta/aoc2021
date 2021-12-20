from run import task1, task2
import pytest
import os

os.chdir(os.path.dirname(__file__))


def test_task1():
    position = task1("example1.txt")
    assert position == 150


def test_task2():
    position = task2("example1.txt")
    assert position == 900
