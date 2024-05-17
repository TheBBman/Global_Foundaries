import matplotlib.pyplot as plt
import numpy as np

# Compare nmos vs pmos

hvoltage = []
hcurrent = []

lvoltage = []
lcurrent = []

with open("0.5um_Data/nmos_data/nmos_0.5_iv_low.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    for line in lines:
        b, a = line.split("      ")
        hvoltage.append(float(b))
        hcurrent.append(float(a))

with open("0.5um_Data/nmos_data/nmos_0.5_iv.txt", 'r') as file:
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

plt.hlines(1e-7, 0, 2, colors='red')

plt.legend(['High Vd', 'Low Vd'])

# plt.ylim(-5e-8, 3e-7)
# plt.xlim(-0.3, 0.5)

plt.show()