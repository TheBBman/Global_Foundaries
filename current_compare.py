import matplotlib.pyplot as plt
import numpy as np

# Compare nmos vs pmos

hvoltage = []
hcurrent = []

lvoltage = []
lcurrent = []

with open("1.8um_Data/pmos_data/pmos_1a_high.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    for line in lines:
        b, a = line.split("      ")
        hvoltage.append(float(b))
        hcurrent.append(float(a))

with open("1.8um_Data/pmos_data/pmos_1a_low.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    for line in lines:
        b, a = line.split("      ")
        lvoltage.append(float(b))
        lcurrent.append(float(a))


plt.plot(hvoltage, hcurrent)

plt.plot(lvoltage, lcurrent)

plt.ylabel("Current Density (A/um)")
plt.xlabel("Gate Voltage Vg")
plt.title("Pmos Current Compare")

plt.hlines(-1e-7, 0, -1, colors='red')

plt.legend(['High Vd: -0.333V', 'Low Vd: -0.385V', 'Voltage Difference: 0.052V'])

plt.ylim(-3e-7, 5e-8)
plt.xlim(-0.5, -0.1)

plt.show()