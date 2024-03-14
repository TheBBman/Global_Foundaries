import matplotlib.pyplot as plt
import numpy as np

# Find subthreshold swing given low Vd

with open("1.8um_Data/nmos_data/nmos_1a_low.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    voltage = []
    current = []

    for line in lines:
        b, a = line.split("      ")
        voltage.append(float(b))
        current.append(float(a))

    plt.plot(voltage, np.abs(current))

    plt.yscale('log') 

    # Subthreshold Swing Extraction

    m, b = np.polyfit(voltage[8:15], np.log10(np.abs(current[8:15])), 1)    #nmos
    #m, b = np.polyfit(voltage[-15:-8], np.log10(np.abs(current[-15:-8])), 1)    #pmos

    x_index = np.arange(-0.1, 0.2, 0.01)    #nmos
    #x_index = np.arange(-0.2, 0.1, 0.01)    #pmos

    plt.plot(x_index, np.power(10, m*x_index) * np.power(10, b))

    plt.ylabel("Absolute Current Density (|A|/um)")
    plt.xlabel("Gate Voltage Vg")
    plt.title("Nmos Subthresh-Swing Extraction")

    plt.legend(['IV-curve', 'Subthreshold Swing: 73.77mV/Dec'])

    print(1000/m)

plt.show()