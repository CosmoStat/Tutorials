FROM jupyter/scipy-notebook

LABEL Description="Scipy Jupyter for Cosmo"

#RUN conda install --yes \
#    numpy \
#    pandas \
#    tini  \
#    ipython \
#    jupyter \
#    cython  \
#    && conda clean -afy
USER root
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get install -y gfortran && \
    apt-get install -y make && \
    apt-get clean

USER jovyan
RUN pip install camb --user && \
    python -c "import camb" && \
    echo "CAMB python wrapper correctly installed"

RUN git clone https://github.com/lesgourg/class_public.git class && \
    cd class/ && \
    make 

RUN python -c "import classy" && \
    echo "CLASS python wrapper correctly installed"


CMD [ "/bin/bash" ]
