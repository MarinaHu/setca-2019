"""
Tests for geom_analysis.py
"""
import geometry_analysis as ga
import pytest

"""A test for the calculate_distance function."""
def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2

"""A test for the bon_check function."""
def test_bond_check_false():
    bond_distance = 3.0
    observed = ga.bond_check(bond_distance)
    assert observed == False

def test_bond_check_true():
    bond_distance = 1.4
    observed = ga.bond_check(bond_distance)
    assert observed == True


def test_bond_check_error():
    bond_length = 'a'

    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_length)
