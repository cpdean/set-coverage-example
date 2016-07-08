from functools import reduce
from itertools import combinations, chain


def _without(objects, i):
    """
    get a list of objects without
    the element at i
    """
    return objects[:i] + objects[i + 1:]


def _union_all(sets):
    return reduce(lambda a, b: a.union(b), sets, set())


def _prune_one(sets):
    """ attempt to remove a single item """
    for i, e in enumerate(sets):
        s = _union_all(_without(sets, i))
        if s.issuperset(e):
            return _without(sets, i)
    return sets


def reduce_sets(sets):
    o = [s for s in sets if s != set([])]
    for n in range(len(sets)):
        o = _prune_one(o)
    return o


def brute_force_set_coverage(sets):
    """
    most naiive approach to set coverage.

    Try all solutions
    Filter non-covering solutions
    Choose smallest solution
    """
    o = [s for s in sets if s != set([])]
    if len(o) == 0:
        return o
    goal_set = _union_all(o)
    solution_generators = [combinations(o, i + 1) for i in range(len(o))]
    all_possible_solutions = chain.from_iterable(solution_generators)
    valid_solutions = [i for i in all_possible_solutions if _union_all(i) == goal_set]
    return list(sorted((i for i in valid_solutions), key=len)[0])
