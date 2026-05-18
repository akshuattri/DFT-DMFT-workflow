# DFT-DMFT-Workflow

DFT+DMFT workflow for correlated electronic structure calculations, Wannier Hamiltonian analysis, Green’s function visualization, and Curie temperature studies.

---

# Overview

This repository contains computational workflows for studying strongly correlated materials using:

- Density Functional Theory (DFT)
- Dynamical Mean Field Theory (DMFT)
- Wannier Hamiltonians
- Green’s function analysis
- Electronic structure calculations

The workflow combines Wannierization and many-body calculations for investigating correlated electronic and magnetic properties.

---

# Repository Structure

```text
DFT-DMFT-Workflow/
│
├── scripts/
│   └── plot_green_function.py
│
├── structures/
│   └── POSCAR
│
├── hamiltonian/
│   └── wannier90_hr.dat
│
├── dmft_data/
│   ├── Giw_up.dat
│   ├── Giw_down.dat
│   ├── Gtau_up.dat
│   ├── Gtau_down.dat
│   └── occupancy.dat
│
├── outputs/
│   ├── dmft.out
│   ├── dmft.err
│   └── dmft_results.h5
│
├── figures/
│
└── README.md
```

---

# Scientific Workflow

## Step 1 — Electronic Structure Calculation

Density Functional Theory (DFT) calculations are performed to obtain the electronic structure of the material system.

Typical input files include:

```text
POSCAR
INCAR
KPOINTS
POTCAR
```

---

## Step 2 — Wannier Hamiltonian Construction

Wannier90 is used to construct the low-energy tight-binding Hamiltonian.

Main Hamiltonian file:

```text
wannier90_hr.dat
```

This Hamiltonian is used as the input for DMFT calculations.

---

# DMFT Calculations

The repository includes DMFT calculations for studying:

- correlated electronic structure,
- finite-temperature properties,
- magnetic behavior,
- and many-body effects.

Generated outputs include:

- Matsubara Green’s functions
- Imaginary-time Green’s functions
- Orbital occupancies
- DMFT solver outputs

---

# Green Function Analysis

The repository includes scripts for plotting:

- Real part of Green’s function
- Imaginary part of Green’s function

Main plotting script:

```text
scripts/plot_green_function.py
```

Example generated figures:

- imaginary_green_function.png
- real_green_function.png

---

# DMFT Data Files

## Matsubara Green Functions

```text
Giw_up.dat
Giw_down.dat
```

## Imaginary-Time Green Functions

```text
Gtau_up.dat
Gtau_down.dat
```

## Orbital Occupancy

```text
occupancy.dat
```

---

# Applications

This workflow can be extended for:

- Curie temperature calculations
- Correlated magnetic systems
- Hubbard model studies
- Strongly correlated materials
- Quantum materials research
- Electronic phase transitions
- Finite-temperature magnetism

---

# Requirements

Typical dependencies include:

```bash
Python
NumPy
Matplotlib
```

Optional packages:

```bash
pymatgen
TRIQS
Wannier90
```

---

# Running the Workflow

## Plot Green Functions

```bash
python scripts/plot_green_function.py
```

---

# Physics Topics

This repository focuses on:

- Dynamical Mean Field Theory (DMFT)
- Strongly Correlated Systems
- Many-Body Physics
- Green’s Functions
- Electronic Structure Theory
- Finite-Temperature Magnetism
- Quantum Materials
- Wannier Hamiltonians

---

# Future Improvements

Potential future developments include:

- Self-energy analysis
- Spectral function calculations
- Multi-orbital DMFT
- Spin-orbit coupling
- Automated DFT → Wannier → DMFT pipelines
- Curie temperature extraction workflows

---

# Author

Akshu Attri

---

# Research Areas

- Computational Condensed Matter Physics
- Electronic Structure Calculations
- Strongly Correlated Systems
- Quantum Materials
- Many-Body Physics
- DFT + DMFT
