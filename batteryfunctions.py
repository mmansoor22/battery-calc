# A simple program containing the functions to calculate
# the charging input, discharging output and
# State-of-Charge (SOC) of the Electric Battery Storage
# equipped with Solar PV module and feeding energy to Electric Load
# Note: Battery charging and discharging is assumed based on just
# one hour basis so the energy stored or energy discharged
# due to input from PV and comparing it with electric load is in kWh unit.

# Function for calculating battery charging with solar PV output (kW) and electric load (kW) as inputs


def char_batt(PV_out, E_load):
    # When solar PV output is greater than electric load, put the surplus into battery
    if PV_out > E_load:
        E_in = PV_out - E_load
        return E_in
    # if the condition is not true

    else:
        return "Can't Charge: PV output is lower than the load"

# Function for calculating battery discharging with solar PV output (kW) and electric load (kW) as inputs


def dischar_batt(PV_out, E_load):
    # When solar PV output is less than electric load, get the insufficient energy from battery
    if PV_out < E_load:
        E_out = abs(PV_out - E_load)
        return E_out
    # if the condition is not true
    else:
        return "Can't Discharge: Electric load is lower than the PV output"

# Function for calculating battery SOC with battery charge (kW), battery discharge (kW) and previous SOC (%) as inputs
def battery_SOC(E_in, E_out, SOC_prev):
    # Capacity of the battery in kWh (fixed)
    batt_cap=60
    # Energy losses in the battery in kWh (fixed as 5% of the batter capacity)
    E_loss = 0.05*batt_cap
    # Calculating the battery's energy stored in kWh
    E_Stored = ((SOC_prev)/100)*batt_cap + E_in - E_out - E_loss
    # Calculating the updated SOC in percentage
    SOC_update = (E_Stored/batt_cap)*100
    # returning the updated SOC by rounding off to 2 decimal points
    return round(SOC_update,2)