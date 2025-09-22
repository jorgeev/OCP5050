# %%
import numpy as np

rho_0 = 1027 # kg/m^3
g = 9.81 # m/s^2
p_atm = 101325 # Pa
drho_dz = -0.005 # kg/m^4
H = -4000 # m

p_const = lambda z: p_atm - rho_0 * g * z
p_var = lambda z: p_atm - g *(0.5 * drho_dz * z**2 + rho_0 * z)

def percentual_diff(p1, p2):
    """
    Calculate the percentual difference between two pressures
    refererence:
    https://www.calculatorsoup.com/calculators/algebra/percent-difference-calculator.php
    https://www.cuemath.com/commercial-math/percent-difference/
    """
    return 100 * (abs(p1 - p2)) / ((p1 + p2) / 2)

print(p_const(0))
print(p_var(0))
print(f"Percentual difference for z=0: {percentual_diff(p_const(0), p_var(0))}")
print(p_const(H))
print(p_var(H))
print(f"Percentual difference for z={H}: {percentual_diff(p_const(H), p_var(H))}")

# %% EoS approxiamtion

gamma_b = 1.1179e-4 # K^-1 m^-1 (nonlinear thermobaric effects)
gamma_c = 1e-5 # K^-2 (cabbeling)

h0 = 0 # m
h4 = -4000 # m

nadw = {
        'S': 34.9, # g/kg
        'Theta': 1, #deg C
        }

aabw = {
        'S': 34.6, # g/kg
        'Theta': -1.5, #deg C
        }


def density_EoS(water_mass,
                gamma_b,
                gamma_c,
                rho_0=1027, # kg/m^3
                theta_0=10, # deg C
                sa_0=35, # g/kg
                g=9.8, # m/s^2
                c_0=1500, # m/s (speed of sound in seawater)
                alpha=1.67e-4, # K^-1
                beta=0.78e-3, # g Kg^-1
                h=0):
    theta_0 = theta_0 + 273.15 # K
    theta = water_mass['Theta'] + 273.15 # K
    S = water_mass['S'] # g/kg
    t1 = g*h/c_0**2
    t2 = alpha * (1 - gamma_b * h) * (theta - theta_0)
    t3 = 0.5 * gamma_c * (theta - theta_0)**2
    t4 = beta * (S - sa_0)
    
    rho_EoS = rho_0 * (1 - t1 - t2 - t3 + t4)
    return rho_EoS

print(f"Density of NADW at h={h0:1f}m: {density_EoS(nadw, gamma_b, gamma_c, h=h0):.4f} kg/m^3")
print(f"Density of AABW at h={h0:1f}m: {density_EoS(aabw, gamma_b, gamma_c, h=h0):.4f} kg/m^3")
print(f"Density of NADW at h={h4:1f}m: {density_EoS(nadw, gamma_b, gamma_c, h=h4):.4f} kg/m^3")
print(f"Density of AABW at h={h4:1f}m: {density_EoS(aabw, gamma_b, gamma_c, h=h4):.4f} kg/m^3")

# If gamma_b = 0
print("If gamma_b = 0")
print(f"Density of NADW at h={h0:1f}m: {density_EoS(nadw, 0.0, gamma_c, h=h0):.4f} kg/m^3")
print(f"Density of AABW at h={h0:1f}m: {density_EoS(aabw, 0.0, gamma_c, h=h0):.4f} kg/m^3")
print(f"Density of NADW at h={h4:1f}m: {density_EoS(nadw, 0.0, gamma_c, h=h4):.4f} kg/m^3")
print(f"Density of AABW at h={h4:1f}m: {density_EoS(aabw, 0.0, gamma_c, h=h4):.4f} kg/m^3")

# %%
