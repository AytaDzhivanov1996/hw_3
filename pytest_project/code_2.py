coll = {"a": {"b": {"c": 3}}}

def set_(coll, path, value):
    coll = {path[0]: {path[1]: {path[2]: value}}}
    return coll
