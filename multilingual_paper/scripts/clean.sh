#!/usr/bin/env bash

#Adapted from https://github.com/facebookresearch/MIXER/blob/master/prepareData.sh

echo 'Cloning Moses github repository (for tokenization scripts)...'
git clone https://github.com/moses-smt/mosesdecoder.git

SCRIPTS=mosesdecoder/scripts
CLEAN=$SCRIPTS/training/clean-corpus-n.perl

DATAPATH=./

perl $CLEAN -ratio 2 $DATAPATH/multilingual src tgt $DATAPATH/multilingual.clean 1 300
