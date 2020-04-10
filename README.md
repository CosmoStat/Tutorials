## Tensorflow
---

> Author: <font color='#f78c40'>[Zaccharie Ramzi](http://www.cosmostat.org/people/zaccharie-ramzi), [Francois Lanusse](http://www.cosmostat.org/people/francois-lanusse)</font>

> Year: 2020

> Email: [zaccharie.ramzi@gmail.com](mailto:zaccharie.ramzi@gmail.com), [francois.lanusse@cea.fr](mailto:francois.lanusse@cea.fr)

This tutorial was intended for the Covid-19 crisis learning-slots in March-April 2020. This intends to be a first introduction to TensorFlow 2.0 not as much from a machine learning
point of view but from an optimization and inverse problem perspective.

We propose two notebooks:

  - **First Steps with TensorFlow**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CosmoStat/Tutorials/blob/tensorflow-tutorial/TensorFlowFirstSteps.ipynb)  
  A short introduction to the basic concepts underpinning TensorFlow, in particular
  automatic differentation.

  - **MRI reconstruction with TensorFlow**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CosmoStat/Tutorials/blob/tensorflow-tutorial/TensorFlowFirstSteps.ipynb)   
  An illustration of how to use TensorFlow in 2 different settings, for the same problem of MRI reconstruction:
- as an optimisation library to perform classical iterative reconstruction
- as a deep learning library to train a CNN to reconstruct fourier undersampled images

### Requirements

All of the notebooks can be run directly on Google Colaboratory, this is highly
recommended.

If you want to run the tutorials locally, you will need Python 3.5+. All the Python requirements are listed in [`requirements.txt`](requirements.txt) except `cython` which is to be installed beforehand. You can then install all the requirements using `pip install -r requirements.txt`.
