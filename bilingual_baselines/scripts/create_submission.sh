#!/bin/bash

# This script will create a submission .zip file from the baseline results
CONFIG_PATH=$1
SRC=$2
TGT=$3

# download the test files
python download_data.py --source_language=$SRC --target_language=$TGT --split=test

for SPLIT in bible, ted, x-wmt
do
    if [[ -f ./data/$SRC-$TGT/test/$SPLIT/$SRC-$TGT.$SRC ]]
    then
        mkdir -p submissions/$SRC-$TGT/$SPLIT
        python -m joeynmt translate $CONFIG_PATH < ./data/$SRC-$TGT/test/$SPLIT/$SRC-$TGT.$SRC > submissions/$SRC-$TGT/$SPLIT/$SRC-$TGT.$TGT
    fi
done

