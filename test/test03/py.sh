#!/bin/bash
currDir=`pwd`

echo "Exposing app to PYTHONPATH:"
echo export PYTHONPATH="${PYTHONPATH}:${currDir}/application"

echo "Activate VENV:"
echo "source ${currDir}/.venv/bin/activate"
