import numpy as np
import matplotlib.pyplot as plt


def line1(x):
    return (4 - 5 * x) / 3


def line2(x):
    return 4 * x - 10


x = np.linspace(-10, 10, 400)

y1 = line1(x)
y2 = line2(x)

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label="5x + 3y = 4")
plt.plot(x, y2, label="4x - y = 10")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphs of the equations 5x + 3y = 4 and 4x - y = 10")

plt.legend()

plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.show()
