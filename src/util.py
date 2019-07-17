def unpack(list):
    keys = set().union(*(d.keys() for d in list))
    return keys