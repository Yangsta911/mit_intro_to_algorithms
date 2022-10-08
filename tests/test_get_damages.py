

from webbrowser import get
import pytest
import algorithms.get_damages as get_damages


@pytest.fixture
def sample_fixture():
    """Setup test fixture"""
    return 1


def test_func(sample_fixture):
    H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
    assert get_damages.get_damages(H) == [4, 5, 6, 3, 3, 1, 4, 1, 1, 1]

def negative_func(sample_fixture):
    H = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert get_damages.get_damages(H) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def test_func2(sample_fixture):
    H = [25, 17, 38, 55, 10, 4, 105, 2000, 7]
    assert get_damages.get_damages(H) == [5, 4, 4, 4, 3, 1, 2, 2, 1]

