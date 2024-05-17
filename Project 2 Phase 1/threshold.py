import matplotlib.pyplot as plt
import numpy as np

# Find threshold voltage given low Vd

with open("1.8um_Data/pmos_data/pmos_1a_low.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    voltage = []
    current = []

    for line in lines:
        b, a = line.split("      ")
        voltage.append(float(b))
        current.append(float(a))

    plt.plot(voltage, current)

    # Threshold Voltage Extraction

    #m, b = np.polyfit(voltage[20:-10], current[20:-10], 1)  #nmos
    m, b = np.polyfit(voltage[14:-20], current[14:-20], 1)  #pmos

    #x_index = np.arange(0.2, 1.0, 0.01)     #nmos
    x_index = np.arange(-0.8, -0.2, 0.01)   #pmos

    plt.plot(x_index, m*x_index + b)

    #plt.hlines(0, 0.2, 0.4)     #nmos
    plt.hlines(0, -0.4, -0.2)   #pmos

    plt.ylabel("Current Density (A/um)")
    plt.xlabel("Gate Voltage Vg")
    plt.title("Pmos Threshold Extraction")

    plt.legend(['IV-curve', 'Threshold Voltage: -0.288V'])

    print(-b/m)

plt.show()