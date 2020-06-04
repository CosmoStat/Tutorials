<a href="http://www.cosmostat.org/" target_="blank"><img src="http://www.cosmostat.org/wp-content/uploads/2017/07/CosmoStat-Logo_WhiteBK.jpg" width="400"></a>

> (not working yet)
> [![Binder](https://mybinder.org/badge_logo.svg)]()

## Cosmology with Python wrappers for Einstein-Boltzmann Codes:
### CAMB and CLASS
---

> Authors: <font color='#f78c40'>[Santiago Casas](http://www.cosmostat.org/people/santiago-casas)</font>  
> Year: 2020  
> Email: [santiago.casas@cea.fr](mailto:santiago.casas@cea.fr)

This tutorial is comprised of a series of <a href="https://jupyter-notebook.readthedocs.io/en/stable/" target_="blanck">Jupyter notebooks</a> with simple demonstrations and exercises on how to use `CAMB` and `CLASS` using python wrappers.
The code is designed for non-experts in the field, therefore it includes relatively
simple explanations of cosmological concepts.
It intends to show a general overview of the things that are possible with Einstein-Boltzmann codes and python.

### Notebooks

1. [Background Cosmology](./Einstein-Boltzmann-Codes/Cosmology-Background.ipynb)
1. [Perturbations and the CMB](./Einstein-Boltzmann-Codes/Cosmology-Perturbations-CMB.ipynb)
1. [Galaxy Clustering and the Fisher Matrix](./Einstein-Boltzmann-Codes/Cosmology-GalaxyClustering.ipynb)
1. [Test Notebook for CAMB and CLASS](./Einstein-Boltzmann-Codes/test_CAMB_CLASS.ipynb)

#### Background Cosmology
In this [notebook](./Einstein-Boltzmann-Codes/Cosmology-Background.ipynb), we will cover the following concepts:
1. What is (precision) Cosmology?
2. General Relativity in 5 minutes using `EinsteinPy`
3. The Hubble equation (self-made)
3. The Hubble equation with `CAMB` and `CLASS`
4. Cosmological Distances

#### Perturbations and the CMB
In this [notebook](./Einstein-Boltzmann-Codes/Cosmology-Perturbations-CMB.ipynb), we will cover the following concepts:
1. Quick introduction to the Cosmic Microwave Background.
2. Computing the angular power spectra from `CAMB` and `CLASS`.
3. Interactive comparison of cosmological parameters with Planck data.
3. Transfer functions, growth and growth rate.

#### Galaxy Clustering and the Fisher Matrix
In this [notebook](./Einstein-Boltzmann-Codes/Cosmology-GalaxyClustering.ipynb), we will cover the following concepts:
1. Quick introduction to Galaxy Clustering with spectroscopic redshifts.
2. Building and plotting the GC model with `CAMB` and `CLASS`.
3. Quick introduction to Fisher Matrix forecasts.
3. An example of a 2-dimensional GC Fisher Matrix.

### How to install using Docker

In order to run the tutorial notebooks and to have the Boltzmann codes installed, without problems, we will use Docker containers.
If you haven't installed [Docker](www.docker.com), check their [website for installation instructions](https://docs.docker.com/get-docker/).
If you are interested in more details about Docker, check our CosmoStat tutorial on [Docker for Data Scientists](https://cosmostat.github.io/Tutorials/docker/docker-introduction/#0).

1. Pull the docker image that can be found [here](https://hub.docker.com/repository/docker/santiagocasas/einstein-boltzmann-codes)

   `docker pull santiagocasas/einstein-boltzmann-codes`

2. Clone this repository and checkout into the `boltzmann` branch.

    `git clone https://github.com/santiagocasas/Tutorials/tree/boltzmann`

3. Change directory to `Tutorials/Einstein-Boltzmann-Codes`.

4. Enter the container by doing:

    `docker run -p 8888:8888 -v ${PWD}:/home/jovyan/work/:rw -it santiagocasas/einstein-boltzmann-codes`

5. Check that you see the `class` and `work` folders by typing `ls` inside the docker terminal.

6.  Start a jupyter notebook instance by typing `jupyter notebook` on the terminal.
    If a browser window does not open, copy and paste the link that appears on the terminal prompt into your favorite browser.
    
7.  To test if the installation worked, run all the cells in the `test_CAMB_CLASS.ipynb` notebook, which you will find in the repo under the `work/`  directory. 


### Installing manually and locally
#### Download and install all requirements 

*  Recommended: `gcc` and `gfortran` compilers. [Binaries](https://gcc.gnu.org/wiki/GFortranBinaries) for all platforms.
* <a href="https://camb.readthedocs.io/en/latest/" target_="blank"> CAMB Python installation </a>
* <a href="https://github.com/lesgourg/class_public" target_="blank"> CLASS manual installation </a>
* <a href="https://www.python.org/" target_="blank">Python</a> (require >=3.6)
* <a href="https://www.cython.org/" target_="blank"> Cython</a> (require >=3.6)
* <a href="http://jupyter.org/" target_="blank">Jupyter</a> (recommend >=1.0.0)
* <a href="https://matplotlib.org/" target_="blank">Matplotlib</a> (recommend >=3.0.3)
* <a href="http://www.numpy.org/" target_="blank">NumPy</a> (recommend >=1.16.2)
* <a href="https://pandas.pydata.org/" target_="blank">Pandas</a> (recommend >= 0.24.0)
* <a href="https://www.scipy.org/" target_="blank">SciPy</a> (recommend >=1.2.1)

#### Run the Test Notebook to check that everything has been installed correctly
