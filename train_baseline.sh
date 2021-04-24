#!/bin/bash

# language codes for the source and target language
SRC=$1
TGT=$2

# get the joeynmt setup
git clone https://github.com/joeynmt/joeynmt.git
pip3 install joeynmt/.
pip install torch==1.8.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

# download the all the data from corpus
python download_data.py --source_language $SRC --target_language $TGT

# get access to the files under joeynmt. NOTE: May require device password
sudo chmod 777 joeynmt/scripts/build_vocab.py

# preprocess the data (load, tokenize, clean up etc)
python3 process_data.py $SRC $TGT

# start the training process
cd joeynmt; python3 -m joeynmt train configs/transformer_$SRC$TGT.yaml