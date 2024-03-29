<a href="http://www.cosmostat.org/" target_="blank"><img src="http://www.cosmostat.org/wp-content/uploads/2017/07/CosmoStat-Logo_WhiteBK.jpg" width="400"></a>
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-9-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

# CosmoStat Tutorials
---

CosmoStat is committed to the philosophy of reproducible research, endeavouring
to provide source code and data for all publications. In this spirit, we have
additionally put significant effort into providing useful educational
materials. The aim being to provide other researchers with an in-depth
understanding of the various tools we use in our work.

We always welcome new tutorial requests, just click [here](https://github.com/CosmoStat/Tutorials/issues/new?assignees=&labels=tutorial+request&template=tutorial-request.md&title=%5BTutorial%5D+Your+idea+for+a+tutorial).

## Contents

1. [Career Development](#Career-Development)
1. [Cosmology](#Cosmology)
1. [Data Science](#Data-Science)
1. [Software Carpentries](#Software-Carpentries)

### Career Development

1. **[Presentation Tips](https://cosmostat.github.io/Tutorials/presentation_tips/presentation_tips/index.html)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/presentations) [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/playlist?list=PLquvp9RIoLGCmfAZTOKJz7qDO0NqCnMAV)    
   *Authors:* [@pettorin](https://github.com/pettorin)   
   This tutorial provides tips on how to adapt presentations for different goals. The tutorial is mainly meant for scientists, but several tips can be useful for other types of talks.

### Cosmology

1. **[Cosmology with Python wrappers for Einstein-Boltzmann Codes](https://github.com/CosmoStat/Tutorials/tree/boltzmann)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/boltzmann) [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=EMpCxUvF3lc)    
    *Authors:* [@santiagocasas](https://github.com/santiagocasas)  
    This tutorial is comprised of a series of Jupyter notebooks with simple demonstrations and exercises on how to use `CAMB` and `CLASS` using python wrappers. The code is designed for non-experts in the field, therefore it includes relatively simple explanations of cosmological concepts. It intends to show a general overview of the things that are possible with Einstein-Boltzmann codes and python.  

2. **[Power Spectrum](http://github.com/CosmoStat/Tutorials/tree/power-spectrum)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](http://github.com/CosmoStat/Tutorials/tree/power-spectrum) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CosmoStat/Tutorials/blob/power-spectrum/WL_power_spectrum.ipynb)  
   *Authors:* [@b-remy](https://github.com/b-remy), [@dlanzieri](https://github.com/dlanzieri), [@EiffL](https://github.com/EiffL)  
   This tutorial presents how to compute a power spectrum from a lensing map (in the flat sky approximation) and how to compute the corresponding theory spectrum using a cosmology code.
   
### Data Science

1. **[Introduction to Python](https://github.com/CosmoStat/Tutorials/tree/python)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/python) [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=cbekcGxm70Q&list=PLquvp9RIoLGBFfsz8dqzPtLeaEngHYybM) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CosmoStat/Tutorials/python)  
    *Authors:* [@sfarrens](https://github.com/sfarrens),  [@santiagocasas](https://github.com/santiagocasas)  
  * [Tutorial 1: Beginner Topics](https://github.com/CosmoStat/Tutorials/tree/python#tutorial-1-beginner-topics)
    The objective of this tutorial is to provide a first look at Python for beginners. The level is aimed at individuals with little or no experience whatsoever with Python. Experienced users are unlikely to benefit from this tutorial.
  * [Tutorial 2: Intermediate and Advanced Topics](https://github.com/CosmoStat/Tutorials/tree/python#tutorial-2-intermediate-and-advanced-topics)
    The objective of this tutorial is to provide a more in-depth look at object-oriented and pythonic coding. The level is aimed at individuals with some experience with Python and good knowledge of basic object types. This tutorial will likely benefit all except the most advanced users.

2. **[Python Optimisation and Memory Management](https://github.com/CosmoStat/Tutorials/tree/profiling)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/profiling)  
  *Authors:* [@sfarrens](https://github.com/sfarrens)  
  This tutorial introduces some techniques for determinisitic and memory profiling of Python scripts, followed by some tips on how to implement some basic optimisation.

3. **[C++](https://github.com/CosmoStat/Tutorials/tree/CPlusPlus)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/CPlusPlus) [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=47Ldg6i2B8Y&list=PLquvp9RIoLGD5yDykupoCueNp2EHEjuZB)  
  *Authors:* [@kansal9](https://github.com/kansal9)  
  This tutorial aims to help newcomers learn C++ and solve their programming problems. It is assumed that readers are already familiar with C, or at least that they do not have any difficulty reading C code. In other words, those who have experience in C and peo·ple who desire to quickly understand the features of modern C++ in a short period of time are well suited to follow this tutorial.

4. **[Sparsity](https://github.com/CosmoStat/Tutorials/tree/ada)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/ada) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CosmoStat/Tutorials/ada)  
  *Authors:* [@sfarrens](https://github.com/sfarrens)  
  This tutorial is comprised of a series of Jupyter notebooks that demonstrate how the tools implemented in sparsity work as well as showing the applicability of these tools to various simple problems.

5. **[Low-Rank](https://github.com/CosmoStat/Tutorials/tree/low-rank)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/low-rank) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CosmoStat/Tutorials/low-rank)  
  *Authors:* [@sfarrens](https://github.com/sfarrens)  
  The objective is to provide a beginner level introduction to the concept of low-rank approximation, in particular as a regularisation method for solving linear inverse problems.

6. **[TensorFlow](https://github.com/CosmoStat/Tutorials/tree/tensorflow-tutorial)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/tensorflow-tutorial)  
   *Authors:* [@zaccharieramzi](https://github.com/zaccharieramzi), [@EiffL](https://github.com/EiffL)  
   * *First Steps with TensorFlow*: [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=kawHQpxytLo) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CosmoStat/Tutorials/blob/tensorflow-tutorial/TensorFlowFirstSteps.ipynb)  
   A short introduction to the basic concepts underpinning TensorFlow, in particular automatic differentation.
   * *MRI reconstruction with TensorFlow*: [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=HqNm5fowdTU) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CosmoStat/Tutorials/blob/tensorflow-tutorial/MRIReconstructionWithTensorflow.ipynb)  
   An illustration of how to use TensorFlow to solve a toy MRI reconstruction problem using classical iterative reconstructions, and a deep learning approach.  

7. **[Blind Source Separation](https://github.com/RCarloniGertosio/bss_tutorial)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/RCarloniGertosio/bss_tutorial) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RCarloniGertosio/bss_tutorial/master)  
   *Authors:* [@RCarloniGertosio](https://github.com/RCarloniGertosio)  
   The goal of this tutorial is to present Blind Source Separation (BSS) problems and the main methods to solve them. This tutorial does not provide in-depth mathematical explanations for every methods; the emphasis is rather on illustrations and intuition.

8. **[Introduction to MCMC and Bayesian inference](https://colab.research.google.com/drive/1EUF7-CwamhAT6wedntStdb4x3dDbihoo?usp=sharing)** |   [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=EfWEGBHeA3k) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EUF7-CwamhAT6wedntStdb4x3dDbihoo?usp=sharing)  
  *Authors:* [@EiffL](https://github.com/EiffL)  
 This tutorial is a practical introduction to Bayesian inference using emcee and
 touching on questions related to measurement errors and covariance.

9. **[Brief tutorial on importance sampling](https://github.com/CosmoStat/Tutorials/tree/is)** |  [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/is)  
  *Authors:* [@martinkilbinger](https://github.com/martinkilbinger)  
 One-page tutorial to show how a sample of points can be importance sampled to obtain a new sampled under a combined posterior distribution.

 https://github.com/CosmoStat/Tutorials/tree/is

### Software Carpentries

1. **[Git Tutorial](https://github.com/zaccharieramzi/git-tuto)** |  [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/zaccharieramzi/git-tuto)  [![slides](https://img.shields.io/badge/slides-google-yellow)](https://docs.google.com/presentation/d/1vfsG__2-T7xJYGKFs9HfPKmaoMN1Je0V0h7gLyiY1AU/edit?usp=sharing) [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=S1A2qSA0TWo)  
  *Authors:* [@zaccharieramzi](https://github.com/zaccharieramzi)    
 This tutorial will help you practice the basics of the GitHub flow and how to work on open source projects.

2. **[Jekyll Tutorial](https://github.com/sfarrens/jekyll_tutorial)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/sfarrens/jekyll_tutorial)  [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=qRxbbSaVW7M)  
  *Authors:* [@sfarrens](https://github.com/sfarrens)  
  The objective of this tutorial is to introduce Jekyll and show you how to build a website that you can host on GitHub for free.

3. **[Make and CMake Tutorial](https://github.com/sfarrens/make-tutorial)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/sfarrens/make-tutorial)  [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=K27-uncFZgM)  
  *Authors:* [@sfarrens](https://github.com/sfarrens)  
  This tutorial is designed to provide a first look at using Make and CMake to build C/C++ projects.

4. **[Introduction to Docker for Data Scientists](https://cosmostat.github.io/Tutorials/docker/docker-introduction)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/docker)  [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=N7cYFfIWjdw)  
  *Authors:* [@EiffL](https://github.com/EiffL)   
  This tutorial demonstrates how to create a Docker container to distribute a complete Jupyter notebook environment.

5. **[Bash and Scripting Tutorial for Researchers](https://github.com/CosmoStat/Tutorials/tree/bash_tutorial/README.md)** | [![github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/CosmoStat/Tutorials/tree/bash_tutorial) [![youtube](https://img.shields.io/badge/-youtube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=NU8dYd3RM-E&t=37s) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CosmoStat/Tutorials/bash_tutorial?filepath=intro.ipynb)  

    *Authors:* [@fadinammour](https://github.com/fadinammour), [@JulienNGirard](https://github.com/JulienNGirard)(screen segment)
    This tutorial gives the key concepts of bash and its scripts to help researchers manage and process their data with more ease.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://sfarrens.github.io"><img src="https://avatars1.githubusercontent.com/u/6851839?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Samuel Farrens</b></sub></a><br /><a href="#content-sfarrens" title="Content">🖋</a> <a href="#ideas-sfarrens" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-sfarrens" title="Maintenance">🚧</a></td>
    <td align="center"><a href="http://www.cosmostat.org/people/santiago-casas"><img src="https://avatars0.githubusercontent.com/u/6987716?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Santiago Casas</b></sub></a><br /><a href="#content-santiagocasas" title="Content">🖋</a> <a href="#ideas-santiagocasas" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://www.cosmostat.org/people/zaccharie-ramzi"><img src="https://avatars1.githubusercontent.com/u/6387497?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Zaccharie Ramzi</b></sub></a><br /><a href="#content-zaccharieramzi" title="Content">🖋</a> <a href="#ideas-zaccharieramzi" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://flanusse.net"><img src="https://avatars0.githubusercontent.com/u/861591?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Francois Lanusse</b></sub></a><br /><a href="#ideas-EiffL" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-EiffL" title="Maintenance">🚧</a> <a href="#content-EiffL" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/kansal9"><img src="https://avatars2.githubusercontent.com/u/35466803?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vanshika Kansal</b></sub></a><br /><a href="#content-kansal9" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/pettorin"><img src="https://avatars1.githubusercontent.com/u/8088350?v=4?s=100" width="100px;" alt=""/><br /><sub><b>pettorin</b></sub></a><br /><a href="#ideas-pettorin" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-pettorin" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/fadinammour"><img src="https://avatars2.githubusercontent.com/u/39698793?v=4?s=100" width="100px;" alt=""/><br /><sub><b>fadinammour</b></sub></a><br /><a href="#ideas-fadinammour" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-fadinammour" title="Content">🖋</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://www.cosmostat.org/people/jgirard/"><img src="https://avatars1.githubusercontent.com/u/10849756?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Julien N Girard</b></sub></a><br /><a href="#content-JulienNGirard" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/RCarloniGertosio"><img src="https://avatars0.githubusercontent.com/u/49195242?v=4?s=100" width="100px;" alt=""/><br /><sub><b>RCarloniGertosio</b></sub></a><br /><a href="#content-RCarloniGertosio" title="Content">🖋</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
