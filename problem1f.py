import matplotlib.pyplot as plt
import numpy as np

# Problem 1f

overdrives = ['0v', '0.2v', '0.4v', '0.6v', '0.8v', '1v']

with open("1.8um_Data/pmos_data/pmos_1a_high.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    voltage = []
    current = []

    for line in lines:
        b, a = line.split("      ")
        voltage.append(float(b))
        current.append(float(a))

    plt.plot([x+0.22 for x in voltage][1:25], [x for x in current][1:25])

plt.legend(['Id v.s. (Vg-Vth) Curve'], loc=4)

for i in overdrives:
    with open("1.8um_Data/pmos_data/pmos_1f_%s.txt" % i, 'r') as file:
        lines = [line.rstrip() for line in file][6:]

        voltage = []
        current = []

        for line in lines:
            b, a = line.split("      ")
            voltage.append(float(b))
            current.append(float(a))

        voltage = voltage[:29]
        current = current[:29]

        voltage.append(0)
        current.append(0)

        plt.plot(voltage, current)

plt.ylabel("Current Density (A/um)")
plt.xlabel("Drain Voltage (Vd)")
plt.title("Nmos Overdrive IV-Curves")

# plt.text(1.5, 1.84e-5, 'Vg - Vth = 1V', rotation=7)
# plt.text(1.6, 1.3e-5, '0.8V', rotation=5)
# plt.text(1.6, 0.84e-5, '0.6V', rotation=3)
# plt.text(1.6, 0.45e-5, '0.4V', rotation=2)
# plt.text(1.6, 0.18e-5, '0.2V', rotation=1)
# plt.text(1.65, 0.4e-6, '0V', rotation=0, fontsize=9)

plt.ylim(-6.8e-6, 0.3e-6)
plt.xlim(-1.55, 0.07)

plt.show()