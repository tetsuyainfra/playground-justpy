#!/bin/bash

# set -x # output execute command
set -e # stop if error code != 0
set -u # stop if access undefined variable

script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
ansible_dir=$(dirname ${script_dir})

USE_PYTHON_VERSION=3.9.6
# USE_PYENV_NAME=infrasite_${USE_PYTHON_VERSION//\./_}
USE_PYENV_NAME=mini_web

echo "USE_PYTHON_VERSION=${USE_PYTHON_VERSION}"
echo "USE_PYENV_NAME=${USE_PYENV_NAME}"

pushd $ansible_dir
  pyenv virtualenv $USE_PYTHON_VERSION $USE_PYENV_NAME
  pyenv local $USE_PYENV_NAME
  python -m pip install --upgrade pip
  pip install remi
  pip install pysimpleguiweb
  pip install justpy
popd
