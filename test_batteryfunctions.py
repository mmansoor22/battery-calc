# This simple program is for testing the battery
# funcions imported from batteryfunctions.py file
# and tested in pytest testing configuration

# Importing the functions
from batteryfunctions import char_batt
from batteryfunctions import dischar_batt
from batteryfunctions import battery_SOC

# Testing the battery charging function
def test_charge_batt():
    assert char_batt(50, 45) == 5

# Testing the battery discharging function
def test_discharge_batt():
    assert dischar_batt(50, 60) == 10

# Testing the battery SOC function
def test_SCO_batt():
    assert battery_SOC(10,5,75) == 78.33