# mlktools

Various tools to support day to day processing and workflows

## Installation

Prefered method of installtion using pipx: <https://pypa.github.io/pipx/>

```
pipx install git+https://github.com/MLKaufman/mlktools.git
```

can aslo be installed with vanilla pip:

```
pip install git+https://github.com/MLKaufman/mlktools.git
```

Once installed can be run using the command:
`mlktools`


## Example Usage

```
 mlktools --help
                                                                                                                                        
 Usage: mlktools [OPTIONS] COMMAND [ARGS]...                                                                                            
                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]             │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the    │
│                                                              installation.                                                           │
│                                                              [default: None]                                                         │
│ --help                                                       Show this message and exit.                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ bashdrop             Create a bash script to drop an LSF HPC job template shell script into a directory.                             │
│ sccleanup            Clean up outputs from CellRanger scRNA-seq processing                                                           │
│ spatialcleanup       Clean up outputs from SpaceRanger Spatial processing                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```