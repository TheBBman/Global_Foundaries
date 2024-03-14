import matplotlib.pyplot as plt
import numpy as np

# Find max transconductance given low Vd

with open("1.8um_Data/nmos_data/nmos_1a_low.txt", 'r') as file:
    lines = [line.rstrip() for line in file][6:]

    voltage = []
    current = []

    for line in lines:
        b, a = line.split("      ")
        voltage.append(float(b))
        current.append(float(a))

    fig, ax1 = plt.subplots()

    ax1.set_ylabel("Current Density (A/um)")
    ax1.set_xlabel("Gate Voltage Vg")
    ax1.plot(voltage, current, color='red')
    ax1.set_ylim(-1e-7, 4.2e-6)
    ax1.tick_params(axis='y', labelcolor='red')

    # Maximum Transconductance

    transconductance = np.gradient(current, voltage)

    ax2 = ax1.twinx()
    ax2.set_ylabel("Transconductance (S/um)")
    ax2.plot(voltage, transconductance)
    ax2.scatter(0.625, 3.5764e-6)
    ax2.tick_params(axis='y', labelcolor='blue')

    fig.tight_layout()
    ax1.legend(['IV-curve'])
    ax2.legend(['Transconductance Curve', 'Max Transconductance:\n3.576e-6 S/um'], loc=4)
    plt.title("Nmos Transconductance")

    print(np.max(transconductance))

plt.show()