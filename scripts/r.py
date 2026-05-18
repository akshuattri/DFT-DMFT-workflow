import os
from ase.io import read
from TB2J.exchange import Exchange
from TB2J.wannier.w90_parser import W90Parser

def run():
    print("--- Starting TB2J for Fe BCC ---")
    
    seedname = "wannier90"
    
    # 1. Load atoms (ASE can usually read .wout if VASP/W90 was recent)
    # If this fails, use a POSCAR file if you have one.
    try:
        atoms = read(f"{seedname}.wout")
    except:
        print("Could not read .wout, trying to find a POSCAR...")
        atoms = read("POSCAR")
    
    print(f"Structure: {atoms.get_chemical_formula()} loaded.")

    # 2. Parse the Wannier90 files
    # This replaces the HWannier call that was failing
    parser = W90Parser(seedname=seedname, posfile=f"{seedname}.wout")
    model = parser.get_model()

    # 3. Setup the Exchange calculation
    # kmesh [7,7,7] is good for a fast check.
    exch = Exchange(
        model=model,
        atoms=atoms,
        efermi=0.0,
        magnetic_elements=['Fe'],
        kmesh=[7, 7, 7]
    )

    print("Calculating Magnetic Exchange (J_ij)...")
    exch.run()

    # 4. Generate Vampire files
    print("Writing outputs for Monte Carlo...")
    exch.write_outputs(output_formats=['vampire'])
    print("\nCheck TB2J_results/Vampire/ for your input files.")

if __name__ == "__main__":
    run()
