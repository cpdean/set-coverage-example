import hypothesis as h
from hypothesis import strategies as st

import setcoverage


def test_example():
    s = [{1}, {1, 2}, {2}]
    assert setcoverage.reduce_sets(s) == [{1, 2}]


@h.given(st.lists(st.sets(st.integers())))
def test_that_output_has_fewer_sets_than_input(sets):
    output = setcoverage.reduce_sets(sets)
    assert len(output) <= len(sets)
