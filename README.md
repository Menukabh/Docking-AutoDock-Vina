### Basic Docking using AutoDock-Vina
## Dock PN3 and PN5 peptides using Autodock-Vina
Reference: https://autodock-vina.readthedocs.io/en/latest/docking_basic.html
https://github.com/pritampanda15/Drug-Designing/blob/main/grid_generation_vina-main/grid.py

The structure of PN3 and PN5 peptides were generated in PEP-FOLD 3.5: https://mobyle.rpbs.univ-paris-diderot.fr/cgi-bin/portal.py#forms::PEP-FOLD3
To get the structure in PEP-FOLD, the seqeunce should be in fasta format
>PN3
Aminoacid_seqeunce_was_typed

PEP-FOLD3 gives different 3D structure in PDB format after uploading amino acid sequences. One of the 3D format could be saved for docking. 
The format saved in PEP-FOLD3 cannot be directly converted to sdf format in babel. So, convert it first to the PDB format in pymol.
Load the struture generated in PEP-FOLD3 and convert it to proper PDB format using the following command 

### Preparation of Ligand

```python
# PyMOL Command for changing the pdb file generated from PEP-FOLD to proper PDB file
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
### Preparation of Receptor
##For blind docking prepare the grid box for the receptor using command

```python
python grid.py
```

##Once the grid box is generated use the command to prepare the receptor. This will generate the grid box and the pdbqt file of the recpetor used for docking.

The dimension of the grid box generated above will be used as a box size and box center.
mk_prepare_receptor.py -i qs_5/ygfb/ygfb.pdb -o qs_5/ygfb/ygfb -p -v \
--box_size 36.069 29.951 35.375 --box_center -3.7934995 3.2364998 -1.8455005


##Perform docking using the Autodock Vina
sbatch docking_P2_yejm.sh

##The output of the autodock Vina would be Binding affinities, RMSD and the different poses of ligand
