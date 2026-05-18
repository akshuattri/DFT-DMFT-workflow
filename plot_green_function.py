import numpy as np
import matplotlib.pyplot as plt

up_data = np.loadtxt("Giw_up.dat")
down_data = np.loadtxt("Giw_down.dat")

omega_up = up_data[:, 0]
real_up = up_data[:, 1]
imag_up = up_data[:, 2]

omega_down = down_data[:, 0]
real_down = down_data[:, 1]
imag_down = down_data[:, 2]

plt.figure(figsize=(8,6))
plt.plot(omega_up, imag_up, label="Im G(iw) Up")
plt.plot(omega_down, imag_down, label="Im G(iw) Down")
plt.xlabel(r"Matsubara Frequency $i\omega_n$")
plt.ylabel(r"Im $G(i\omega_n)$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("imaginary_green_function.png", dpi=300)

plt.figure(figsize=(8,6))
plt.plot(omega_up, real_up, label="Re G(iw) Up")
plt.plot(omega_down, real_down, label="Re G(iw) Down")
plt.xlabel(r"Matsubara Frequency $i\omega_n$")
plt.ylabel(r"Re $G(i\omega_n)$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("real_green_function.png", dpi=300)

plt.show()
