#!/bin/bash

python setup.py bdist_wheel
az extension remove --name fzf
az extension add --yes  --source dist/fzf-*-py2.py3-none-any.whl