from pytest_project.code_2 import set_

coll = coll = {"a": {"b": {"c": 3}}}
def test_set_():
    assert set_(coll, ["a", "b", "c"], 4) == {'a': {'b': {'c': 4}}}
    assert set_(coll, ['x', 'y', 'z'], 5) == {'x': {'y': {'z': 5}}}
