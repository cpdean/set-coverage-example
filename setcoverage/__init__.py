
def _without(objects, i):
    """
    get a list of objects without
    the element at i
    """
    return objects[:i] + objects[i+1:]


def _prune_one(sets):
    """ attempt to remove a single item """
    for i, e in enumerate(sets):
        for s in _without(sets, i):
            if s.issuperset(e):
                return _without(sets, i)
    return sets


def reduce_sets(sets):
    one_removed = _prune_one(sets)
    two_removed = _prune_one(one_removed)
    return two_removed
