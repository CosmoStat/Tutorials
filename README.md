# Bash and Scripting Tutorial for Researchers

The goal of this tutorial is to introduce researchers to bash and scripting. It is a short tutorial that shows major concepts with use cases related to research work.

---
> Authors: <font color='#f78c40'>[Fadi Nammour](http://www.cosmostat.org/people/fadi-nammour) , [Julien N. Girard](https://www.cosmostat.org/people/julien-girard)</font>  
> Year: 2020  
> Email: [fadi.nammour@cea.fr](mailto:fadi.nammour@cea.fr), [julien.girard@cea.fr](mailto:julien.girard@cea.fr) (screen segment)

## Table of Contents

1. [Introduction](./basics.ipynb#indtroduction)
2. [Basics](./basics.ipynb#basics)
3. [Pipeline, pipes and filters](./pipeline.ipynb)
4. [Bash Scripts](./scripting.ipynb)
5. [Screening](./screening.ipynb)
6. Beyond the Scope
7. Acknowledgements
8. Resources


## Launching the Tutorial
To start this tutorial, it is possible to launch it online using Binder with no installation required, or install it and start it locally using Docker as follow:

### Binder
Click on the following icon to launch the tutorial [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fadinammour/bash_intro/master?filepath=intro.ipynb).

### Docker
0. Install [Docker](https://www.docker.com/products/docker-desktop) 


1. Run the following command in a terminal:
`docker run -p 8889:8889 -v ${PWD}:/home/jovyan/:rw -it fadinammour/bash-intro start-notebook.sh --NotebookApp.port=8889 --NotebookApp.token=''`

> *Note 1* The number `8889` appears three times. The first occurence correspond to the port number of the local machine. The second one corresponds to the port of the docker container and the third one is the port of the Jupyter notebook. If you want to change the port numbers, the last two should be the same.

> *Note 2* The empty string argument `''` passed to the `--NotebookApp.token` options shortcuts the token verification step. However it is not recommanded to be used with distant work for security reasons, in that case the option can just be erased.

2. Open the Jupyter notebook in a browser by copying the link that appears in the terminal and pasting it to the browser. In case, the link does not work try entering the following address instead `0.0.0.0:8889`.

> *Note 3* The number `8889` here corresponds to the port number of the local machine. In case this number is changed, it should be also be changed in the previous step.

## Beyond the Scope Topics

Here is a list of functions and concepts that were not covered by this tutorial:

- arithmetical operation
- regular expressions
- bash profil
- aliases
- shabang
- chown
- ssh
- sed
- chmod
- functions
- boolean operations
- wildcards (globbing)
- loops and conditions

For curious readers, these notions are explained in the links of the Resources section.

## Acknowledgements
This work has been made easier thanks to the valuable help and assistance of [Samuel Farren](https://sfarrens.github.io/) and [François Lanusse](http://www.flanusse.net/).

## Resources

This tutorial was inspired by the following:
1. [The Unix Shell lesson](http://swcarpentry.github.io/shell-novice/) part of the data used in the tutorial was taken from this resource.
2. [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)
3. [How to Use Linux Screen](https://linuxize.com/post/how-to-use-linux-screen/)

Additionnal material:
1. [Bash Reference Manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
2. [Bash scripting cheatsheet](https://devhints.io/bash)