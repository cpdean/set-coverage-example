from functools import reduce


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
