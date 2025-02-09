#!/bin/bash
#SBATCH --account=PAS0471
#SBATCH --cpus-per-task=24
#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --output=slurm-autodock-%j.out

##created environment and loaded multiple packages
module load miniconda3/4.10.3-py37
source activate /users/PAS0471/menuka/.conda/envs/alphafold_env_310

##Submit as a script becuase it takes lot of time to run
vina --ligand P1_P2/p2_pymol.pdbqt --receptor yejm/cleaned_yejm.pdbqt \
     --config yejm/cleaned_yejm.box.txt \
     --exhaustiveness 32 \
     --cpu "$SLURM_CPUS_PER_TASK" \
     --out docking_output_P2_yejm.pdbqt 


echo "Done with script"
date