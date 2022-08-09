from root.crawler.stock_info import classify
import pytest


@pytest.mark.parametrize('roe, fcf, expected', [
    (25, 1000, 'A+'),
    (18, 100, 'A'),
    (17, 0, 'B1'),
    (14, 100, 'B2'),
    (11, 0, 'C'),
    (7, 1000, 'C1'),
    (3, 0, 'C2'),
    (0, 0, 'D')])
def test(roe, fcf, expected):
    assert classify(roe, fcf) == expected
#  py.test --cov=./  test_classify.py
