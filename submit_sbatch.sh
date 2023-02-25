#!/bin/bash
#SBATCH --job-name=myjob
#SBATCH -p compute
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
###SBATCH --mem=20G
#SBATCH --time=02:00:00
#SBATCH -o slurm-out_u10.out
#SBATCH -e slurm-err_u10.out
#SBATCH -A bb1153

ulimit -s unlimited

echo Submitted job: $jobid
squeue -u $USER

# determine JOBID
JOBID=`echo $SLURM_JOB_ID |cut -d"." -f1`

#cd <where you want to do your work>

date
python3  IFS_TC_msl_6H.py 
date
