# ADA Sparsity Tutorial

> Author: <font color='#f78c40'>[Samuel Farrens](http://www.cosmostat.org/people/sfarrens)</font>    
> Year: 2018 (updated in 2023)  
> Email: [samuel.farrens@cea.fr](mailto:samuel.farrens@cea.fr)  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CosmoStat/Tutorials/blob/ada/])[![Open In Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CosmoStat/Tutorials/ada)

This tutorial was originally presented at the ninth edition of the
[Astronomical Data Analysis (ADAIX)](http://ada.cosmostat.org/) summer school held in Valencia
in 2018. The objective is to provide a beginner level introduction to the concept of sparsity, in particular as a regularisation method for solving linear inverse problems. The tutorial does not provide an in-depth mathematical background nor detailed explanations for every topic. Tutees should supplement this tutorial with further reading of the various references provided in the notebooks for a more comprehensive understanding of the subject. More information about how cutting-edge sparsity techniques are being applied to astrophysical data is available on the <a href="http://www.cosmostat.org/" target_="blank">CosmoStat website</a>.

This tutorial is comprised of a series of <a href="https://jupyter-notebook.readthedocs.io/en/stable/" target_="blanck">Jupyter notebooks</a> that demonstrate how the tools implemented in sparsity work as well as showing the applicability of these tools to various simple problems.

All code blocks are provided in Python and the number of external packages required to run the examples has be kept to a minimum. With the exception of plotting routines, all of the code has been clearly presented inside the notebooks at least once to avoid the use of any "black boxes" for solving the problems presented.

## Running the notebooks remotely

All of the Jupyter notebooks for the tutorial can be run remotely (i.e. without needing to install anything locally) using either [Google Colab](https://colab.research.google.com/) or [Binder](https://mybinder.org/). Click on either of the badges above to launch one of these services. Note that running the notebooks in this way will require a stable internet connection. Also note that Binder make take several minutes to launch.

## Running the notebooks locally

Alternatively, you can [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or simply [download](https://github.com/CosmoStat/Tutorials/archive/refs/heads/ada.zip) the repository contents to your computer. Once the content is downloaded and all of the requirements have been installed, you will be able to run the notebooks locally without the need of an internet connection.

### Requirements

In order to run the tutorial notebooks locally, you will need to have the following packages installed:

* <a href="https://www.python.org/" target_="blank">Python</a>
* <a href="http://www.numpy.org/" target_="blank">NumPy</a> (recommend v1.24+)
* <a href="https://www.scipy.org/" target_="blank">SciPy</a> (recommend v1.10+)
* <a href="https://matplotlib.org/" target_="blank">Matplotlib</a> (recommend v3.6+)
* <a href="http://jupyter.org/" target_="blank">Jupyter</a> (recommend v1.0+)

All of the packages listed above can easily be installed using either `pip` or <a href="https://docs.conda.io/" target_="blank">Conda</a>.

*e.g.*

```bash
$ pip install numpy scipy matplotlib jupyter
```

or

```bash
$ conda install numpy scipy matplotlib jupyter
```

## List of notebooks

1. [Introduction to Inverse Problems](inverse_problems_1.ipynb)
1. [Introduction to Sparsity I](sparsity_1.ipynb)
1. [Introduction to Sparsity II: Compressed Sensing](sparsity_2_compressed_sensing.ipynb)
1. [Introduction to Sparsity III: Deconvolution](sparsity_3_deconvolution.ipynb)
1. [Introduction to Wavelets](wavelets_1.ipynb)
1. [Exercise Solutions](exercise_solutions.ipynb)

## Acknowledgements

S. Farrens would like to acknowledge the following people for helpful feedback and ideas for producing this tutorial: Fred Ngolè-Mboula and Jean-Luc Starck.
