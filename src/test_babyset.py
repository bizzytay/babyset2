# test_babyset.py
# Demonstrates unit testing using the pytest module.
# pytest must be installed through pip.
#py.test to run 
from baby_set import BabySet
import pytest

def test_init():
    bset = BabySet([2, 4, 4])
    assert bset.size() == 2

def test_init_empty():
    bset = BabySet()
    assert bset.size() == 0

def test_add():
    bset = BabySet([2, 4, 4])
    bset.add(4)
    assert bset.size() == 2

def test_addSeq():
    baby = BabySet([2,4,4])
    baby.addSeq([1,2,3])
    assert baby.size()==4

def test_get():
    baby = BabySet([2,4,4])
    with pytest.raises(KeyError):
         baby.get(1)
    baby.get(2)

def test_remove():
    baby = BabySet([2,4,4])
    with pytest.raises(KeyError):
        baby.remove(1)
    baby.remove(2)

def test_clear():
    baby = BabySet([2,4,4])
    baby.clear()
    assert baby.size()==0
