# Docking-AutoDock-Vina
## Dock PN3 and PN5 using Autodock-Vina
Reference: https://github.com/pritampanda15/Drug-Designing/blob/main/grid_generation_vina-main/grid.py

The structure of PN3 and PN5 peptides were generated in PEP-FOLD 3.5: https://mobyle.rpbs.univ-paris-diderot.fr/cgi-bin/portal.py#forms::PEP-FOLD3
TO get the structure: 
> PN3
Aminoacid_seqeunce_was_typed

PEP-FOLD3 gives different 3D structure in pdb format. One of the 3D format was saved. 
The format saved in PEP-FOLD3 cannot  be directly converted to sdf format in babel. So, convert it first to the PDB format in pymol.
Load the struture generated in PEP-FOLD3 and convert it to PDB format using command save PN5.pdb

##convert pdb to sdf file in babel
obabel PN5/PN5.pdb -O PN5/PN5.sdf

##Change the implicit hydrogen to explicit hydrogen
python scripts/explicit.py

##Change the ligand to the pdbqt format
python scripts/prepare_ligand.py
