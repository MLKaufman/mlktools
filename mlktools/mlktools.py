import os

import typer
from rich import print

app = typer.Typer()

@app.command()
def newproject():
    print("Creating new project")
    print(os.getcwd())
    os.mkdir("pipeline")
    os.mkdir("raw_data")

@app.command()
def sccleanup(item: str):
    """Clean up outputs from CellRanger scRNA-seq processing"""
    #check that we are in root directory of cellranger outs
    #
    print(f"Creating item: {item}")

@app.command()
def spatialcleanup():
    """Clean up outputs from SpaceRanger Spatial processing"""
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)
    # check that we are in root directory of spaceranger outs
    # create a new directory for spaceranger_results
    # create subdirectories for each sample A B C D aggregate
    # create outs subdirectory for each sample
    # move all files from spaceranger outs to appropriate subdirectory
        # A_*.html, cloupe.cloupe, filtered_feature_bc_matrix/, filtered_feature_bc_matrix.h5, spatial
    for root, dirs, files in os.walk('.', topdown=True):
        dirs.clear() #with topdown true, this will prevent walk from going into subs
        for file in files:
            #do some stuff
            print(file)

@app.command()
def bashdrop(filename: str, queue: str = "rna", cores: int = 12, ram: int = 50, email: str= "michael.kaufman@cuanschutz.edu", command: str = "echo 'hello world'"):
    """Create a bash script to drop an LSF HPC job template shell script into a directory."""
    f = open(filename + ".sh", "w+")
    f.writelines(f"""#! /usr/bin/env bash
### -- specify queue -- 
#BSUB -q rna

### -- set the job Name -- 
#BSUB -J {filename}

### -- cores -- 
#BSUB -n {cores} 

### -- specify memory -- 
#BSUB -R "span[hosts=1]"
#BSUB -R "select[mem>100] rusage[mem=100]"

### -- set walltime limit: hh:mm -- 
#BSUB -W 48:00 

### -- set the email address -- 
#BSUB -u {email}

### -- send notification at completion -- 
#BSUB -N 

### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o {filename}_output_bsub.out 
#BSUB -e {filename}_error_bsub.err

### -- load modules or software required --

### -- run the command --
{command}""")
    f.close()



if __name__ == "__main__":
    app()