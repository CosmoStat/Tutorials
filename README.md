<a href="http://www.cosmostat.org/" target_="blank"><img src="http://www.cosmostat.org/wp-content/uploads/2017/07/CosmoStat-Logo_WhiteBK.jpg" width="400"></a>

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CosmoStat/Tutorials/master)

# CosmoStat Tutorials
---

CosmoStat is committed to the philosophy of reproducible research, endeavouring
to provide source code and data for all publications. In this spirit, we have
additionally put significant effort into providing useful educational
materials. The aim being to provide other researchers with an in-depth
understanding of the various tools we use in our work.


## Contents
---

1. [Set Up](#Set-Up)
1. [Introduction to Python](./python/README.md)
   * [Requirements](./python/README.md#Requirements)
   * [Notebooks](./python/README.md#Notebooks)
1. [Sparsity](./ada/README.md)
   * [Requirements](./ada/README.md#Requirements)
   * [Notebooks](./ada/README.md#Notebooks)
   * [Acknowledgements](./ada/README.md#Acknowledgements)
1. [Low-Rank](./low-rank/README.md)
   * [Requirements](./low-rank/README.md#Requirements)
   * [Notebooks](./low-rank/README.md#Notebooks)
   * [Acknowledgements](./low-rank/README.md#Acknowledgements)

## Set Up
---

### Requirements

Each tutorial has its own set of requirements, but all require Python 3.5 or higher.

* <a href="https://www.python.org/" target_="blank">Python</a> (require >=3.5)


### Running Remotely

All of the tutorials can be run remotely by launching the repository
[Binder](https://mybinder.org/v2/gh/CosmoStat/Tutorials/master). No further set
up is required.

### Running Locally

In order to run the tutorials offline, please follow these steps:

1. Download or clone the GitHub repository.

    <img src="http://www.cs.williams.edu/~dbarowy/cs334s18/assets/tutorials/github/github-clone-button.png" width="300">

    *e.g.*

    ```bash
    git clone https://github.com/CosmoStat/Tutorials.git
    ```

2. Install the tutorial dependencies.

    This can be done using `pip` as follows:

    ```bash
    pip install -r requirements.txt
    ```

      or using `conda` as follows:

    ```bash
    conda env create -f environment.yml
    conda activate cstutorial
    ```

3. Finally, the notebooks can be launched by running:

    ```bash
    jupyter notebook
    ```
