FROM jupyter/base-notebook:python-3.7.6

LABEL Description="Jupyter Bash"

USER root
RUN apt-get update && \
    apt-get -y install screen && \
    apt-get install tree && \
    apt-get update && \
    apt-get clean

RUN export TERM=vt100

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

USER ${NB_USER}

RUN  conda install -c conda-forge bash_kernel

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
