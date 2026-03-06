#!/bin/bash

pip install --upgrade pip

# install CPU-only PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu

# install other dependencies
pip install -r requirements.txt