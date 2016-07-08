
def reduce_sets(sets):
    if sets == []:
        return sets
    # create a set of the items found
    o = set()
    for s in sets:
        o = o.union(s)
    return [o]
