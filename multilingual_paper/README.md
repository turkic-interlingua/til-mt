
# Evaluating Multiway Multilingual NMT in Turkic Languages (WMT 2021)

### Results (Bilingual vs MNMT)

|        |            | In-Domain Test |      |       |      | X-WMT Test |      |       |      |
|--------|------------|----------------|------|-------|------|------------|------|-------|------|
| Pairs  | Train size | Bilingual      |      | MNMT  |      | Bilingual  |      | MNMT  |      |
|        |            | BLEU           | Chrf | BLEU  | Chrf | BLEU       | Chrf | BLEU  | Chrf |
| en-tr  | 35.8M      | 31.45          | 0.51 | 33.09 | 0.51 | 16.04      | 0.55 | 26.74 | 0.56 |
| tr-en  | 35.8M      | 31.37          | 0.50 | 35.48 | 0.52 | 20.39      | 0.51 | 24.66 | 0.55 |
| ru-uz  | 1.3M       | 53.12          | 0.76 | 44.73 | 0.71 | 6.58       | 0.41 | 6.70  | 0.42 |
| uz-ru  | 1.3M       | 55.39          | 0.76 | 46.42 | 0.71 | 6.08       | 0.36 | 9.16  | 0.39 |
| en-kk  | 564.8K     | 24.53          | 0.54 | 18.92 | 0.49 | 7.82       | 0.40 | 9.92  | 0.43 |
| kk-en  | 564.8K     | 29.17          | 0.51 | 24.67 | 0.48 | 12.00      | 0.42 | 15.71 | 0.44 |
| az-en  | 548.9K     | 26.65          | 0.48 | 20.47 | 0.42 | 12.01      | 0.41 | 20.41 | 0.49 |
| en-az  | 548.9K     | 34.73          | 0.56 | 15.27 | 0.42 | 6.79       | 0.38 | 9.71  | 0.43 |
| en-uz  | 529.6K     | 45.95          | 0.66 | 27.80 | 0.51 | 6.34       | 0.40 | 9.89  | 0.42 |
| uz-en  | 529.6K     | 38.72          | 0.58 | 32.44 | 0.50 | 4.81       | 0.24 | 14.45 | 0.45 |
| ba-ru  | 523.7K     | 46.02          | 0.69 | 40.59 | 0.64 | 24.39      | 0.58 | 24.57 | 0.57 |
| ru-ba  | 523.7K     | 51.26          | 0.74 | 43.44 | 0.67 | 24.31      | 0.59 | 23.13 | 0.56 |
| az-tr  | 410.1K     | 23.47          | 0.48 | 18.40 | 0.43 | 10.61      | 0.43 | 19.63 | 0.48 |
| tr-az  | 410.1K     | 29.97          | 0.53 | 15.71 | 0.42 | 7.78       | 0.39 | 8.21  | 0.42 |
| en-ky  | 312.6K     | 21.66          | 0.44 | 14.54 | 0.38 | 2.33       | 0.27 | 4.64  | 0.34 |
| ky-en  | 312.6K     | 24.96          | 0.42 | 18.01 | 0.38 | 4.65       | 0.29 | 10.87 | 0.39 |
| ky-ru  | 293.7K     | 19.63          | 0.40 | 16.30 | 0.38 | 5.23       | 0.30 | 14.08 | 0.44 |
| ru-ky  | 293.7K     | 18.57          | 0.43 | 14.82 | 0.40 | 4.42       | 0.35 | 10.35 | 0.45 |
| ba-en  | 34.3K      | 21.51          | 0.36 | 17.79 | 0.37 | 0.32       | 0.19 | 10.55 | 0.40 |
| en-ba  | 34.3K      | 17.78          | 0.33 | 17.29 | 0.35 | 0.16       | 0.14 | 8.35  | 0.34 |
| en-kaa | 17.1K      | 15.34          | 0.40 | 19.42 | 0.46 | 0.31       | 0.19 | 2.82  | 0.27 |
| kaa-en | 17.1K      | 22.82          | 0.43 | 21.95 | 0.48 | 1.04       | 0.21 | 10.21 | 0.38 |
| ru-sah | 9.2K       | 13.26          | 0.35 | 5.46  | 0.19 | 0.12       | 0.16 | 4.64  | 0.17 |
| sah-ru | 9.2K       | 16.35          | 0.36 | 13.11 | 0.26 | 0.42       | 0.18 | 4.41  | 0.25 |
| en-sah | 8.1K       | 13.45          | 0.36 | 4.98  | 0.18 | 0.04       | 0.14 | 3.46  | 0.12 |
| sah-en | 8.1K       | 22.19          | 0.40 | 5.90  | 0.23 | 0.16       | 0.21 | 3.38  | 0.24 |



### Reproducing the results from the paper

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
8. Configure your hyperparameters and start the training
```
fairseq-train \
    data-bin \
    --arch transformer_wmt_en_de --share-decoder-input-output-embed \
    --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
    --lr 5e-4 --lr-scheduler inverse_sqrt --warmup-updates 40000 \
    --dropout 0.3 --weight-decay 0.0001 \
    --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
    --max-tokens 4096 \
    --eval-bleu \
    --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \
    --eval-bleu-detok moses \
    --eval-bleu-remove-bpe \
    --eval-bleu-print-samples \
    --best-checkpoint-metric bleu --maximize-best-checkpoint-metric
```
9. Test your models
```
gcloud beta compute scp --project "tilcorpus-301123" --zone "us-central1-a" til-mt:~/finetune/checkpoint_best.pt ./finetune

```
11. Upload to HuggingFace
