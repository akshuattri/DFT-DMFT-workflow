import numpy as np
import matplotlib.pyplot as plt

# ==============================
# PARAMETERS
# ==============================
nk = 80
emin, emax = -10, 10

# ==============================
# READ hr.dat
# ==============================
def read_hr(filename):
    with open(filename, 'r') as f:
        f.readline()
        nw = int(f.readline())
        nr = int(f.readline())

        deg = []
        while len(deg) < nr:
            deg += list(map(int, f.readline().split()))

        R, H = [], []

        for i in range(nr):
            Hmat = np.zeros((nw, nw), dtype=complex)

            for j in range(nw*nw):
                line = f.readline().split()
                Rx, Ry, Rz = map(int, line[:3])
                m = int(line[3])-1
                n = int(line[4])-1
                re = float(line[5])
                im = float(line[6])

                if j == 0:
                    R.append((Rx, Ry, Rz))

                Hmat[m,n] = re + 1j*im

            H.append(Hmat)

    return np.array(R), np.array(H)

# ==============================
# H(k)
# ==============================
def Hk(k, R, H):
    Hk = np.zeros_like(H[0], dtype=complex)
    for i,(Rx,Ry,Rz) in enumerate(R):
        phase = np.exp(1j*2*np.pi*(k[0]*Rx + k[1]*Ry + k[2]*Rz))
        Hk += H[i]*phase
    return Hk

# ==============================
# HIGH-SYMMETRY POINTS (BCC)
# ==============================
kpts = {
    "H": [0.5, -0.5, 0.5],
    "P": [0.25, 0.25, 0.25],
    "N": [0.0, 0.5, 0.0],
    "G": [0.0, 0.0, 0.0]
}

path = ["H","P","N","G","H","N","G","P"]

# ==============================
# BUILD PATH
# ==============================
klist = []
kticks = []
labels = []
dist = 0

for i in range(len(path)-1):
    k1 = np.array(kpts[path[i]])
    k2 = np.array(kpts[path[i+1]])

    for t in np.linspace(0,1,nk):
        k = k1*(1-t) + k2*t
        klist.append(k)

    kticks.append(dist)
    labels.append(path[i])
    dist += nk

kticks.append(dist)
labels.append(path[-1])

# ==============================
# LOAD
# ==============================
R, H = read_hr("wannier90_hr.dat")

# ==============================
# COMPUTE BANDS
# ==============================
bands = []

for k in klist:
    eig = np.linalg.eigvalsh(Hk(k, R, H))
    bands.append(eig)

bands = np.array(bands)

# ==============================
# SHIFT FERMI (approx)
# ==============================
Ef = np.median(bands)
bands -= Ef

# ==============================
# PLOT
# ==============================
plt.figure(figsize=(7,5))

for i in range(bands.shape[1]):
    plt.plot(bands[:,i], color='blue', linewidth=0.6)

for t in kticks:
    plt.axvline(t, linestyle='--', color='gray')

plt.axhline(0, linestyle='--', color='red')

plt.xticks(kticks, labels)
plt.ylabel("Energy (eV)")
plt.title("Fe BCC Band Structure (Wannier90)")

plt.ylim(emin, emax)
plt.xlim(0, len(klist))

plt.tight_layout()
plt.show()
