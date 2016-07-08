import setcoverage


def test_example():
    s = [{1}, {1, 2}, {2}]
    assert setcoverage.reduce_sets(s) == [{1, 2}]
