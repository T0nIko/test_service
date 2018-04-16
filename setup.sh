#!/usr/bin/env bash

if ! [ -x $(command -v python3) ];
then
    echo "Python3 is not available."
    exit -1
else
    py_version=$(python3 -V)
    echo "Using $py_version"
fi

if ! [ -x $(command -v pip3) ];
then
    echo "Pip3 is not available."
    exit -1
else
    pip_version=$(pip3 -V)
    echo "Using $pip_version"
fi

requirements=./requirements.txt

if ! [ -r $requirements ];
then
    echo "requirements.txt not found/not readable."
    exit -1
fi

python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
