import matplotlib.pyplot as plt

temps = ['25C', '75C', '150C']
plt.figure()

for temp in temps:
    with open("Abrupt/%s/IV_curve.txt" % temp, 'r') as file:
        lines = [line.rstrip() for line in file]

    voltage = []
    current = []

    for line in lines:
        b, a = line.split("        ")
        voltage.append(float(b))
        current.append(float(a))

    plt.plot(voltage, current)

plt.title("5µm x 0.5µm Abrupt PN Junction IV-Curve")
plt.ylim(1e-17, 1e-1)
plt.yscale("log")
plt.xlabel("Voltage (V)")
plt.ylabel("Current Density (A/µm)")
plt.legend(temps)
plt.show()