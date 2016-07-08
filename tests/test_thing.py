import hypothesis as h
from hypothesis import strategies as st
from functools import reduce

from setcoverage import reduce_sets


def test_example():
    s = [{1}, {1, 2}, {2}]
    assert reduce_sets(s) == [{1, 2}]


@h.given(st.lists(st.sets(st.integers())))
def test_that_output_has_fewer_sets_than_input(sets):
    output = reduce_sets(sets)
    assert len(output) <= len(sets)


@h.given(st.lists(st.sets(st.integers())))
def test_no_items_lost(sets):
    union = lambda a, b: a.union(b)
    all_input = reduce(union, sets, set())
    all_output = reduce(union, reduce_sets(sets), set())
    assert all_input == all_output
