## Tensorflow
---

> Author: <font color='#f78c40'>[Zaccharie Ramzi](http://www.cosmostat.org/people/zaccharie-ramzi), [Francois Lanusse](http://www.cosmostat.org/people/francois-lanusse)</font>

> Year: 2020

> Email: [zaccharie.ramzi@gmail.com](mailto:zaccharie.ramzi@gmail.com), [francois.lanusse@cea.fr](mailto:francois.lanusse@cea.fr)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kmw_6O39vP9u9EA06-lIZXHc_eRbkWqK)


This tutorial was intended for the Covid-19 crisis learning-slots in March-April 2020.
It presents the use of TensorFlow in 2 different settings, for the same problem of MRI reconstruction:
- as an optimisation library to perform classical iterative reconstruction
- as a deep learning library to train a CNN to reconstruct fourier undersampled images

### Requirements

In order to run the tutorial you will need Python 3.5+.

All the Python requirements are listed in [`requirements.txt`](requirements.txt) except `cython` which is to be installed beforehand.
You can then install all the requirements using `pip install -r requirements.txt`.
