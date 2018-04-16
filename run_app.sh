#!/usr/bin/env bash

if ! [ -x $(command -v gunicorn) ];
then
    echo "Unable to run gunicorn. Check your virtual environment."
    exit -1
else
    gunicorn -c gunicorn.py app:app
fi
