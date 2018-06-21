import pytest
from hypothesis import given
import hypothesis.strategies as st

def diction(keys, values):
    try:
        if type(keys) is not list or type(values) is not list:
            raise TypeError('Input argument is not a list')
    except TypeError:
        print('Argument is not a list.')
    else:
        result = dict.fromkeys(keys, None)
        result.update(zip(keys, values))
        return result

#asserts
def test_assert():
    assert diction([1, 2, 3, 4],['A','B','C'])=={1: 'A', 2: 'B', 3: 'C', 4: None}
    assert diction([1,2,3], 3)==None
    assert diction(3,['A','B','C'])==None
    assert diction([],['A','B','C'])=={}

#param
@pytest.mark.parametrize("a,b,expected",[
    ([1,2,3],['A','B','C','D'], {1: 'A', 2: 'B', 3: 'C'}),
    ([1,2,3], 3, None),
    (3,['A','B','C'],None),
    ([],['A','B','C'],{})
])
def test_param(a, b, expected):
    assert diction(a,b)==expected
    assert diction([1,2,3], 3)==None
    assert diction(3,['A','B','C'])==None
    assert diction([],['A','B','C'])=={}

#hypothesis
@given(st.lists(), st.lists())
def test_diction(a, b):
    assert type(diction(a,b)) == dict
    assert len(diction(a,b)) == len(a)