#!/usr/bin/env bash

if ! [ -f ./venv/bin/activate ];
then
    echo "Unable to find virtual environment."
    exit -1
else
    if [ "$(command -v deactivate)" ];
    then
        deactivate
    else
        echo "Virtual enviroment isn't active."
        exit -1
    fi
fi
