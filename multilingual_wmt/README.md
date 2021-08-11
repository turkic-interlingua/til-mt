1. Download the entire corpus

```
# BE CAREFUL! This object is extremely large in size (> 40 gigabytes)
# to download the already sampled version, refer to ...
python scripts/download_data.py
```

2. Merge the data using the sampler script
```
python sampler.py corpus/train 1.25
```
3. Create the dev set using the bin dev script

```
python3 sampler_dev.py
```

4. Clean the data using the perl script
```
source clean.sh
```

5. Train the sentencepiece bpe on the data (or sample from the data)
```
source create_apply_spm.sh
```
7. Preprocess your data using the fairseq functions

```
fairseq-preprocess --source-lang src --target-lang tgt \
    --trainpref ./multilingual.bpe \
    --validpref ./mnmt_bin_dev/low/low.bpe \
    --workers 50
```
8. Configure your hyperparameters
```

```
9. Start the training
10. Test your models
11. Upload to HuggingFace
