"""Unit tests for Programming Assignment #4 engineering calculations.

Programmer: [Your name]
Course: ENSC 201, Fall 2026
Version: 1.0
Date: 2026-10-13
Sources: PA4 starter tests; OpenAI ChatGPT assisted with code,
documentation, debugging, and tests.
"""

# An assert checks whether a condition is true. If it is false, Python raises
# AssertionError and pytest marks that test as failed. A test passes when it
# finishes without an assertion failure or another error. np.isclose compares
# floating-point values with a tolerance for small rounding differences.
# After correcting the two formulas and the power test, rerun the full suite
# to check that all six test functions pass.

import numpy as np

from engineering_formulas import (
    calculate_circle_area,
    calculate_density,
    calculate_force,
    calculate_kinetic_energy,
    calculate_power,
    celsius_to_fahrenheit,
)


def test_calculate_force():
    """Check ordinary, zero, fractional, and negative acceleration cases."""
    assert calculate_force(10, 2) == 20
    assert calculate_force(0, 100) == 0
    assert np.isclose(calculate_force(4.0, 0.5), 2.0)
    assert calculate_force(3, -2) == -6


def test_calculate_density():
    """Check ordinary, zero-mass, and fractional density cases."""
    # Original inputs: mass 10, volume 2. Expected 5; actual was 0.2.
    # The expected density was correct, so repair the formula, not this test.
    assert np.isclose(calculate_density(10, 2), 5.0)
    assert np.isclose(calculate_density(0, 4), 0.0)
    assert np.isclose(calculate_density(2.5, 0.5), 5.0)
    assert np.isclose(calculate_density(1, 4), 0.25)


def test_calculate_power():
    """Check ordinary, zero-current, and fractional power cases."""
    # Original inputs: current 3, voltage 12. Actual 36; expected was 15.
    # Power is current times voltage, so 36 is correct. Fix the test to 36;
    # leave the correct multiplication in calculate_power unchanged.
    assert calculate_power(3, 12) == 36
    assert calculate_power(0, 120) == 0
    assert np.isclose(calculate_power(0.5, 9.0), 4.5)
    assert np.isclose(calculate_power(0.1, 0.2), 0.02)


def test_calculate_kinetic_energy():
    """Check ordinary, stationary, fractional, and negative velocity cases."""
    # Original inputs: mass 5, velocity 4. Expected 40; actual was 10.
    # The expected energy was correct; fix the missing velocity square.
    assert np.isclose(calculate_kinetic_energy(5, 4), 40.0)
    assert np.isclose(calculate_kinetic_energy(5, 0), 0.0)
    assert np.isclose(calculate_kinetic_energy(2.5, 2.0), 5.0)
    assert np.isclose(calculate_kinetic_energy(5, -4), 40.0)


def test_calculate_circle_area():
    """Check unit, zero, fractional, and larger radii against known areas."""
    assert np.isclose(calculate_circle_area(1), 3.141592653589793)
    assert np.isclose(calculate_circle_area(0), 0.0)
    assert np.isclose(calculate_circle_area(0.5), 0.7853981633974483)
    assert np.isclose(calculate_circle_area(2), 12.566370614359172)


def test_celsius_to_fahrenheit():
    """Check freezing, boiling, negative, and fractional temperatures."""
    assert np.isclose(celsius_to_fahrenheit(0), 32.0)
    assert np.isclose(celsius_to_fahrenheit(100), 212.0)
    assert np.isclose(celsius_to_fahrenheit(-40), -40.0)
    assert np.isclose(celsius_to_fahrenheit(37.5), 99.5)
