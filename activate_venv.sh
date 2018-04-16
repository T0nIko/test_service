#!/usr/bin/env bash

if ! [ -f ./venv/bin/activate ];
then
    echo "Unable to find virtual environment."
    exit -1
else
    source ./venv/bin/activate
fi
