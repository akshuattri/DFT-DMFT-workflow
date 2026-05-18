import numpy as np
import matplotlib.pyplot as plt

# ==============================
# PARAMETERS (TUNED)
# ==============================
U = 3.3              # tuned interaction
kB = 8.617e-5

beta_list = np.linspace(2, 80, 25)   # wide temperature range
nk = 40

# ==============================
# DISPERSION (simple cubic)
# ==============================
kmesh = np.linspace(-np.pi, np.pi, nk)

def epsilon(kx, ky, kz):
    return -2*(np.cos(kx) + np.cos(ky) + np.cos(kz))

# ==============================
# STABLE FERMI FUNCTION
# ==============================
def fermi(E, beta):
    x = beta * E
    return np.where(x > 50, 0.0,
           np.where(x < -50, 1.0,
           1.0/(np.exp(x)+1)))

# ==============================
# DMFT LOOP
# ==============================
T_list = []
M_list = []

for beta in beta_list:

    print("beta =", beta)

    m = 0.1   # initial seed

    for it in range(60):

        n_up = 0
        n_dn = 0

        for kx in kmesh:
            for ky in kmesh:
                for kz in kmesh:

                    ek = epsilon(kx, ky, kz)

                    # mean-field splitting
                    e_up = ek - U*m
                    e_dn = ek + U*m

                    n_up += fermi(e_up, beta)
                    n_dn += fermi(e_dn, beta)

        n_up /= nk**3
        n_dn /= nk**3

        m_new = n_up - n_dn

        # mixing
        m = 0.6*m + 0.4*m_new

    T = 1.0 / (beta * kB)

    T_list.append(T)
    M_list.append(m)

# ==============================
# SORT (important)
# ==============================
T = np.array(T_list)
M = np.array(M_list)

idx = np.argsort(T)
T = T[idx]
M = M[idx]

# ==============================
# ESTIMATE Tc (INTERPOLATION)
# ==============================
Tc = None

for i in range(len(M)-1):
    if M[i] > 0 and M[i+1] <= 0:
        Tc = T[i] + (0 - M[i])*(T[i+1]-T[i])/(M[i+1]-M[i])
        break

# ==============================
# SAVE
# ==============================
np.savetxt("single_band_M_vs_T.dat",
           np.column_stack([T, M]),
           header="T(K) M")

# ==============================
# PLOT
# ==============================
plt.figure(figsize=(6,5))

plt.plot(T, M, 'o-', label="Magnetization")

plt.xlabel("Temperature (K)")
plt.ylabel("Magnetization")
plt.title("Single-band DMFT (mean-field Tc extraction)")

if Tc is not None:
    plt.axvline(Tc, linestyle='--', color='red', label=f"Tc ≈ {Tc:.0f} K")

plt.legend()
plt.grid()
plt.tight_layout()

plt.savefig("single_band_Tc.png", dpi=300)
plt.show()

# ==============================
# OUTPUT
# ==============================
print("\n==========================")
print("Estimated Tc =", Tc, "K")
print("Fe experimental Tc ≈ 1043 K")
print("==========================")
