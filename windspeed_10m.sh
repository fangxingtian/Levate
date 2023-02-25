#!/bin/bash
#SBATCH --job-name=myjob
#SBATCH -p compute
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
###SBATCH --mem=20G
#SBATCH --time=02:00:00
#SBATCH -o slurm-out.out
#SBATCH -e slurm-err.out
#SBATCH -A bb1153

ulimit -s unlimited

echo Submitted job: $jobid
squeue -u $USER

# determine JOBID
JOBID=`echo $SLURM_JOB_ID |cut -d"." -f1`

#cd <where you want to do your work>
cd /scratch/b/b381639/IFS
date

#cdo merge [ u10_daily_tco1279-orca025_r360x180.nc v10_daily_tco1279-orca025_r360x180.nc ] components.nc
#cdo 'expr,ws=sqrt(u10*u10+v10*v10)' components.nc windspeed10.nc
cdo -sqrt -add -sqr u10_daily_tco1279-orca025.nc -sqr v10_daily_tco1279-orca025.nc windspeed10_daily_tco1279-orca025.nc
date
