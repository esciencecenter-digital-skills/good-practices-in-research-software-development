"""
This module contains unit tests for the conversion_mod module.
"""

from conversion_mod import celsius_to_fahrenheit, celsius_to_kelvin, check_unit_validity


def test_celsius_to_fahrenheit():
    """
    Test the celsius_to_fahrenheit function.
    """
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(20) == 68
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(20) == 68
    assert isinstance(celsius_to_fahrenheit(-1000), str)


def test_check_unit_validity():
    """
    Test the check_unit_validity function.
    """
    assert check_unit_validity("C") is True
    assert check_unit_validity("F") is True
    assert check_unit_validity("K") is True
    assert check_unit_validity("X") is False


def test_celsius_to_kelvin():
    """
    Test the celsius_to_kelvin function.
    """
    assert celsius_to_kelvin(20) == 293.15
    assert celsius_to_kelvin(0) == 273.15
