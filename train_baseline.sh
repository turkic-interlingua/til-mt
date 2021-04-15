#!/bin/bash

SRC=$1
TGT=$2

git clone https://github.com/joeynmt/joeynmt.git
pip3 install joeynmt/.
pip install torch==1.8.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

python3 download_data.py $SRC $TGT

sudo chmod 777 joeynmt/scripts/build_vocab.py

python3 process_data.py $SRC $TGT

cd joeynmt; python3 -m joeynmt train configs/transformers_$SRC$TGT.yaml