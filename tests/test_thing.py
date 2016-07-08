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


@h.given(st.lists(st.sets(st.integers())))
def test_all_sets_come_from_input(sets):
    output = reduce_sets(sets)
    forbidden_sets = [s for s in output if s not in sets]
    assert len(forbidden_sets) == 0


@h.given(st.lists(st.sets(st.integers())))
def test_no_duplicate_sets(sets):
    output = reduce_sets(sets)
    for e_ix, e in enumerate(output):
        for s_ix, s in enumerate(output):
            if e_ix == s_ix:
                continue
            assert e != s, "duplicate in {}".format(output)


@h.given(st.lists(st.sets(st.integers())))
def test_no_empty_sets(sets):
    output = reduce_sets(sets)
    assert set([]) not in output


@h.given(st.lists(st.sets(st.integers())))
def test_no_subsets(sets):
    output = reduce_sets(sets)
    for e_ix, e in enumerate(output):
        for s_ix, s in enumerate(output):
            if e_ix == s_ix:
                continue
            assert not e.issubset(s), "subset found in {}".format(output)


@h.given(st.lists(st.sets(st.integers(min_value=-1, max_value=5), max_size=3), max_size=8))
def test_no_sibling_superset_cover_a_set_in_output(sets):
    union = lambda a, b: a.union(b)
    without = lambda o, i: o[:i] + o[i + 1:]
    output = reduce_sets(sets)
    for i, e in enumerate(output):
        siblings_superset = reduce(union, without(output, i), set())
        assert not siblings_superset.issuperset(e)


def test_hard_coverage():
    s = [
        {1,   2}, {3,   4},
        {1}, {2,   3}, {4}
    ]
    assert reduce_sets(s) == [{1, 2}, {3, 4}]
