import matplotlib.pyplot as plt
import numpy as np

# Parts 1b, 1c, 1e

with open("1.8um_Data/nmos_data/nmos_1a_low.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    voltage = []
    current = []

    for line in lines:
        b, a = line.split("      ")
        voltage.append(float(b))
        current.append(float(a))

    plt.plot(voltage, current)

    #plt.yscale('log') #Take absolute value of current if pmos

    ## Threshold Voltage Extraction

    # m, b = np.polyfit(voltage[:-20], current[:-20], 1)

    # x_index = np.arange(-1.5, -0.2, 0.01)

    # plt.plot(x_index, m*x_index + b)
    # plt.hlines(0, -0.4, -0.2)

    # print(-b/m)

    ## Subthreshold Swing Extraction

    # m, b = np.polyfit(voltage[-15:-6], np.log10(np.abs(current[-15:-6])), 1)

    # x_index = np.arange(-0.25, 0.2, 0.01)

    # plt.plot(x_index, np.power(10, m*x_index) * np.power(10, b))

    # print(1000/m)

    ## Maximum Transconductance

    transconductance = np.gradient(current, voltage)

    plt.plot(voltage, transconductance)

    print(np.max(transconductance))

plt.show()