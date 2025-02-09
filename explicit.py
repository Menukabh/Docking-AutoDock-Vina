import os
from rdkit import Chem

sdf_file = "/fs/ess/PAS0471/Menuka/autodock_vina/P1_P2/p2_pymol.sdf"

if os.path.exists(sdf_file):
    mol = Chem.SDMolSupplier(sdf_file)[0]
    if mol is not None:
        # Add explicit hydrogens
        mol_with_h = Chem.AddHs(mol)

        # Write the molecule back to an SDF file
        writer = Chem.SDWriter("//fs/ess/PAS0471/Menuka/autodock_vina/P1_P2/p2_with_h.sdf") 
        writer.write(mol_with_h)
        writer.close()

        print("Explicit hydrogens added and saved to P2_with_h.sdf")
    else:
        print(f"Failed to load the molecule from {sdf_file}.")
else:
    print(f"File {sdf_file} does not exist.")
