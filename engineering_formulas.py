"""Engineering calculations for Programming Assignment #4.

Programmer: Michael Friesen
Course: ENSC 201, Fall 2026
Version: 1.0
Date: 2026-10-13
Sources: PA4 starter code; OpenAI ChatGPT assisted with code,
documentation, debugging, and tests.
"""

import math


def calculate_force(mass, acceleration):
    """Calculate force using Newton's second law.

    Args:
        mass (float): Nonnegative mass in kilograms.
        acceleration (float): Signed acceleration in meters per second squared.

    Returns:
        float: Force in newtons.
    """
    return mass * acceleration


def calculate_density(mass, volume):
    """Calculate density from mass and volume.

    Args:
        mass (float): Nonnegative mass in kilograms.
        volume (float): Positive volume in cubic meters.

    Returns:
        float: Density in kilograms per cubic meter.

    Raises:
        ZeroDivisionError: If volume is zero.
    """
    # The starter returned 0.2 for (10, 2), but 10 kg / 2 m^3 is 5.
    # Its division was reversed; divide mass by volume, then rerun tests.
    return mass / volume


def calculate_power(current, voltage):
    """Calculate electrical power.

    Args:
        current (float): Current in amperes.
        voltage (float): Voltage in volts.

    Returns:
        float: Electrical power in watts.
    """
    return current * voltage


def calculate_kinetic_energy(mass, velocity):
    """Calculate translational kinetic energy.

    Args:
        mass (float): Nonnegative mass in kilograms.
        velocity (float): Signed velocity in meters per second.

    Returns:
        float: Kinetic energy in joules.
    """
    # The starter returned 10 for (5, 4), while the expected energy is 40.
    # Kinetic energy is one-half mass times velocity squared; add the square.
    return 0.5 * mass * velocity ** 2


def calculate_circle_area(radius):
    """Calculate a circle's area.

    Args:
        radius (float): Nonnegative radius in meters.

    Returns:
        float: Area in square meters.
    """
    return math.pi * radius ** 2


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit.

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (9 / 5) * celsius + 32


def main():
    """Reserve an entry point for optional manual testing; return None."""
    pass


if __name__ == "__main__":
    main()
