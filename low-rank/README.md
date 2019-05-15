## Low-Rank Approximation
---

> Author: <font color='#f78c40'>[Samuel Farrens](http://www.cosmostat.org/people/sfarrens)</font>    
> Year: 2018  
> Email: [samuel.farrens@cea.fr](mailto:samuel.farrens@cea.fr)  

The objective is to provide a beginner level introduction to the concept of low-rank approximation, in particular as a regularisation method for solving linear inverse problems. The tutorial does not provide an in-depth mathematical background nor detailed explanations for every topic. Tutees should supplement this tutorial with further reading of the various references provided in the notebooks for a more comprehensive understanding of the subject. More information about how cutting-edge sparsity techniques are being applied to astrophysical data is available on the <a href="http://www.cosmostat.org/" target_="blank">CosmoStat website</a>.

This tutorial is comprised of a <a href="https://jupyter-notebook.readthedocs.io/en/stable/" target_="blanck">Jupyter notebook</a> that demonstrate how the low-rank approximation works as well as showing the applicability of this tools to various simple problems.

All code blocks are provided in Python (support for >=3.5) and the number of external packages required to run the examples has be kept to a minimum. All of the code has been clearly presented inside the notebook at least once to avoid the use of any "black boxes" for solving the problems presented.

### Requirements

In order to run the tutorial notebooks tutees will need to have the following installed:

* <a href="https://www.python.org/" target_="blank">Python</a> (require >=3.5)
* <a href="http://www.numpy.org/" target_="blank">NumPy</a> (recommend >=1.16.2)
* <a href="https://www.scipy.org/" target_="blank">SciPy</a> (recommend >=1.2.1)
* <a href="https://www.astropy.org/" target_="blank">Astropy</a> (recommend >=3.1.2)
* <a href="https://matplotlib.org/" target_="blank">Matplotlib</a> (recommend >=3.0.3)
* <a href="http://jupyter.org/" target_="blank">Jupyter</a> (recommend >=1.0.0)

All of the packages listed above can easily be installed using either `pip` or <a href="https://www.anaconda.com/" target_="blank">Anaconda</a>.

*e.g.*

```bash
$ pip install numpy scipy astropy matplotlib jupyter
```

or

```bash
$ conda install numpy scipy astropy matplotlib jupyter
```

### Notebooks

1. [Introduction to Low-Rank Approximation](./low-rank.ipynb)

### Acknowledgements

S. Farrens would like to acknowledge the following people for helpful feedback and ideas for producing this tutorial: Fred Ngolè-Mboula.
