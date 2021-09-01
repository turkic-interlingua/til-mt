#!/usr/bin/env bash

#Adapted from https://github.com/facebookresearch/MIXER/blob/master/prepareData.sh

git clone https://github.com/google/sentencepiece.git 
cd sentencepiece
mkdir build
cd build
cmake ..
make -j $(nproc)
sudo make install
#sudo update_dyld_shared_cache
sudo ldconfig -v

cd ../..

src=src
tgt=tgt
DATAPATH=./
DEV_PATH=./mnmt_bin_dev

spm_train --input="$DATAPATH/multilingual.src, $DATAPATH/multilingual.tgt" --model_prefix="64k_bpe" \
    --vocab_size=64000 \
    --user_defined_symbols="<2alt>,<2az>,<2ba>,<2cjs>,<2crh>,<2cv>,<2gag>,<2kaa>,<2kjh>,<2kk>,<2krc>,<2kum>,<2ky>,<2sah>,<2slr>,<2tk>,<2tr>,<2tt>,<2tyv>,<2ug>,<2uum>,<2uz>,<2en>,<2ru>" \
    --model_type=bpe \
    --num_threads=64 \
    --split_digits=True \
    --byte_fallback=True \
    --train_extremely_large_corpus=True \
    --character_coverage=0.9995

for l in $src $tgt; do
    spm_encode --model=64k_bpe.model --output_format=piece < $DATAPATH/multilingual.clean.$l > $DATAPATH/multilingual.bpe.$l
done

for l in $src $tgt; do
    spm_encode --model=64k_bpe.model --output_format=piece < $DEV_PATH/high/high.$l > $DEV_PATH/high/high.bpe.$l
done

for l in $src $tgt; do
    spm_encode --model=64k_bpe.model --output_format=piece < $DEV_PATH/medium/medium.$l > $DEV_PATH/medium/medium.bpe.$l
done

for l in $src $tgt; do
    spm_encode --model=64k_bpe.model --output_format=piece < $DEV_PATH/low/low.$l > $DEV_PATH/low/low.bpe.$l
done
