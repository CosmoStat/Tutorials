## Importance sampling
---

> Author: <font color='#f78c40'>[Martin Kilbinger](http://www.cosmostat.org/people/kilbinger)</font>    
> Year: 2022  
> Email: [martin.killbinger@cea.fr](mailto:martin.killbinger@cea.fr)  

[notebook](./importance_sampling.ipynb)

This is a very brief tutorial about how importance sampling for Bayesian parameter inference.
Specifically, it describes the case where an existing sample (e.g. a Monte-Carlo Markov chain) can be importance-sampled
to obtain samples under a joint posterior distribution.

For a more general tutorial of Bayesian paremeter inference see the <a href="https://colab.research.google.com/drive/1EUF7-CwamhAT6wedntStdb4x3dDbihoo?usp=sharing">Introduction to MCMC and Bayesian inference</a> linked from <a href="https://github.com/CosmoStat/Tutorials/" target_="blank">CosmoStat Tutorial site</a>.

This tutorial contains a single <a href="https://jupyter-notebook.readthedocs.io/en/stable/" target_="blanck">Jupyter notebook</a> with description and executable code.

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

1. [Introduction to Low-Rank Approximation](https://mybinder.org/v2/gh/CosmoStat/Tutorials/master?filepath=%2Flow-rank%2Flow-rank.ipynb)
