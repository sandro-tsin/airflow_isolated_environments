# Use Apache Airflow as the base image
FROM apache/airflow:2.7.3

# maintainer of the project
LABEL maintainer="Aleksander Tsinamdzgvrishvili"

# Switch to ROOT user for installing mandatory packages
USER root

# Install mandatory packages
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        vim \
        git \
        curl \
        zlib1g-dev \
        libreadline-dev \
        libssl-dev \
        libsqlite3-dev \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        liblzma-dev \
        libffi-dev \
        python3-openssl \
        libbz2-dev \
        libpq-dev \
        gcc \
        python3-distutils \
 && apt-get autoremove -yqq --purge \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Switch back to the default Airflow user
USER airflow

# Install pyenv and pyenv-virtualenv
RUN curl -fsSL https://pyenv.run | bash

# Set up pyenv environment variables
ENV PYENV_ROOT="/home/airflow/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

# Initialize pyenv and pyenv-virtualenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Install Python 3.12 using pyenv
RUN pyenv install 3.12.0

# Create a virtual environment using pyenv
RUN pyenv virtualenv 3.12.0 isolated_vertial_env

# Activate the virtual environment and install required Python packages
RUN bash -c 'source ~/.bashrc && eval "$(pyenv init -)" && eval "$(pyenv virtualenv-init -)" && \
    pyenv shell great_expectation_env && export PIP_USER=false && pip install --upgrade pip && \
    pip install great_expectations==1.3.7 psycopg2-binary==2.9.9 sqlalchemy==1.4.49 airflow-provider-great-expectations==0.2.7'