import numpy as np

# ==============================
# PARAMETERS
# ==============================
nk = 80

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
# BCC PATH
# ==============================
kpts = {
    "H": [0.5, -0.5, 0.5],
    "P": [0.25, 0.25, 0.25],
    "N": [0.0, 0.5, 0.0],
    "G": [0.0, 0.0, 0.0]
}

path = ["H","P","N","G","H","N","G","P"]

# ==============================
# BUILD K-PATH
# ==============================
klist = []
kdist = [0]
dist = 0

for i in range(len(path)-1):
    k1 = np.array(kpts[path[i]])
    k2 = np.array(kpts[path[i+1]])

    for t in np.linspace(0,1,nk):
        k = k1*(1-t) + k2*t
        klist.append(k)

    dist += nk
    kdist.append(dist)

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
Ef = np.sort(bands.flatten())[len(bands.flatten())//2]
bands -= Ef

# ==============================
# WRITE band.dat
# ==============================
with open("band.dat", "w") as f:
    for i in range(bands.shape[1]):
        for k in range(len(klist)):
            f.write(f"{k} {bands[k, i]:.6f}\n")
        f.write("\n")

print("band.dat generated ✔")
