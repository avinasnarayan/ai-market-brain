#!/bin/bash

pip install --upgrade pip

# Install CPU PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
pip install -r requirements.txt