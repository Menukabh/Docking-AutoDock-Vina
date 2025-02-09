# Docking-AutoDock-Vina
## Dock PN3 and PN5 using Autodock-Vina
Reference: https://github.com/pritampanda15/Drug-Designing/blob/main/grid_generation_vina-main/grid.py

The structure of PN3 and PN5 peptides were generated in PEP-FOLD 3.5: https://mobyle.rpbs.univ-paris-diderot.fr/cgi-bin/portal.py#forms::PEP-FOLD3
To get the structure: 
> PN3
Aminoacid_seqeunce_was_typed

PEP-FOLD3 gives different 3D structure in PDB format after uploading amino acid sequences. One of the 3D format could be saved for docking. 
The format saved in PEP-FOLD3 cannot  be directly converted to sdf format in babel. So, convert it first to the PDB format in pymol.
Load the struture generated in PEP-FOLD3 and convert it to proper PDB format using command 

### PyMOL Commands for Visualization

```python
# Load a PDB file
load my_protein.pdb
save PN5.pdb
```

```bash
##convert pdb to sdf file in babel
obabel PN5/PN5.pdb -O PN5/PN5.sdf
```

```python
##Change the implicit hydrogen to explicit hydrogen
python scripts/explicit.py
##Change the ligand to the pdbqt format
python scripts/prepare_ligand.py
```

Download the PDB format of the receptor from the PDB website "https://www.rcsb.org/"
##For blind docking prepare the grid box for the receptor using command grid.py

##Once the grid box is generated use the command to prepare the receptor. THis will generate the grid box and the pdbqt file of the recpetor

##Perfrom docking using the Autodock Vina
##The output of the autodock Vina would be Binding affinities, RMSD and the different poses of ligand
