# Replication files 

This repository contains replication files for the article:

- Ferrari, Schlegel, and Arretche (2023) "O que pensa o brasileiro sobre a federação? Centralização e crise de confiança pós-2013". *DADOS* (accepted).

# Citation:


```latex
@article{ferrari2023pensa,
    author = {Diogo Ferrari and Rogerio Schlegel and Marta Arretche},
    title = {O que pensa o brasileiro sobre a federação? Centralização e crise de confiança pós-2013},
    year={2023},
    journal = {DADOS},
    volume = {(just accepted)},
    issue = {},
    doi = {},
    url = {},
}
```

# This repository contains

1. Tables and figures
2. The scripts used to generate the analysis, tables, and figures
3. Data set(s) used in the analyses

# Instructions for replication

### Option 1: Download the files manually

For replication, make sure you have the following folder structure in place
```ascii
.
├── data
│   └── final                        <- folder with data used in the analysis; codebook is here
├── man                              <- folder with the manuscript (limited if copyright applies)
│   ├── figures-and-tables           <- tables and figures (in .pdf, .png. etc) used in the manuscript
│   └── supp-material                <- online supplement (OS)
│       └── figures-and-tables       <- tables and figures (in .pdf, .png. etc) used in the OS
├── src                              <- scripts for replication
│   └── model                        <- folder with the replication scripts
└── README.md                        <- this file
```

Then, run the scripts in the folder `model`. 

### Option 2: Cloning from github

1. Donwload the replication files or clone the repository by running the following command in your terminal:
``` shell
git clone https://github.com/DiogoFerrari/**`this repo`**
```
2. Run the scripts in the folder `model`

