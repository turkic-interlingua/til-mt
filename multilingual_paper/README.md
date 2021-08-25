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
