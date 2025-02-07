def unique(lst):
    return [x for i, x in enumerate(lst) if x not in lst[:i]]
