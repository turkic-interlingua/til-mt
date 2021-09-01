import os
import pandas as pd
import csv
from sacremoses import MosesTokenizer
from os import path
import sys

# select the source and target language code
source_language = sys.argv[1]
target_language = sys.argv[2]

# this is for bilingual
experiment_name = "bilingual_baseline"

experiment_folder = f"experiments/{source_language}-{target_language}-{experiment_name}"

if not os.path.isdir(experiment_folder):
    os.makedirs(experiment_folder)

def load_data(folder):
    source_path = f"{folder}/{source_language}-{target_language}/{source_language}-{target_language}.{source_language}" 
    target_path = f"{folder}/{source_language}-{target_language}/{source_language}-{target_language}.{target_language}" 

    source = open(source_path, "r").readlines()
    target = open(target_path, "r").readlines()

    assert len(source) == len(target)   
    source, target = tokenize(source, target)

    df = pd.DataFrame(zip(source, target), columns=['source_sentence', 'target_sentence'])
    return df

def tokenize(source, target):
    mt = MosesTokenizer()

    for i in range(len(source)):
        source[i] = mt.tokenize(source[i], return_str=True)
    
    for i in range(len(target)):
        target[i] = mt.tokenize(target[i], return_str=True)

    return source, target
    
def build_subword_bpe():
    
    # Learn BPEs on the training data.
    data_path = os.path.join("joeynmt", "data", source_language + target_language) # Herman! 
    if not os.path.isdir(data_path):
        os.makedirs(data_path)

    print("learning bpe on the train files...")
    os.system(f"subword-nmt learn-joint-bpe-and-vocab --input data/train/en-tr/en-tr.{source_language} data/train/en-tr/en-tr.{target_language} -s 32000 -o {data_path}/bpe.codes.32000 --write-vocabulary vocab.{source_language} vocab.{target_language}")

    print("applying the bpe files to the data...")
    # Apply BPE splits to the development and test data.
    os.system(f"subword-nmt apply-bpe -c {data_path}/bpe.codes.32000 --vocabulary vocab.{source_language} < data/train/en-tr/en-tr.{source_language} > {data_path}/train.bpe.{source_language}")
    os.system(f"subword-nmt apply-bpe -c {data_path}/bpe.codes.32000 --vocabulary vocab.{target_language} < data/train/en-tr/en-tr.{target_language} > {data_path}/train.bpe.{target_language}")

    os.system(f"subword-nmt apply-bpe -c {data_path}/bpe.codes.32000 --vocabulary vocab.{source_language} < data/dev/en-tr/en-tr.{source_language} > {data_path}/dev.bpe.{source_language}")
    os.system(f"subword-nmt apply-bpe -c {data_path}/bpe.codes.32000 --vocabulary vocab.{target_language} < data/dev/en-tr/en-tr.{target_language} > {data_path}/dev.bpe.{target_language}")
    
    os.system(f"subword-nmt apply-bpe -c {data_path}/bpe.codes.32000 --vocabulary vocab.{source_language} < data/test/en-tr/en-tr.{source_language} > {data_path}/test.bpe.{source_language}")
    os.system(f"subword-nmt apply-bpe -c {data_path}/bpe.codes.32000 --vocabulary vocab.{target_language} < data/test/en-tr/en-tr.{target_language} > {data_path}/test.bpe.{target_language}")
    
    os.system(f"joeynmt/scripts/build_vocab.py joeynmt/data/{source_language}{target_language}/train.bpe.{source_language} joeynmt/data/{source_language}{target_language}/train.bpe.{target_language} --output_path joeynmt/data/{source_language}{target_language}/vocab.txt")



def build_config():
    # Create the config
    name = source_language + target_language

    config = f"""
    name: "{name}_transformer"

    data:
        src: "{source_language}"
        trg: "{target_language}"
        train: "data/{name}/train.bpe"
        dev:   "data/{name}/dev.bpe"
        test:  "data/{name}/test.bpe"  # change this to data/{name}/test2.bpe so that you can test it on Ted Talks
        level: "bpe"
        lowercase: False
        max_sent_length: 128
        src_vocab: "data/{name}/vocab.txt"
        trg_vocab: "data/{name}/vocab.txt"

    testing:
        beam_size: 5
        alpha: 1.0
        sacrebleu:                      # sacrebleu options
            remove_whitespace: True     # `remove_whitespace` option in sacrebleu.corpus_chrf() function (defalut: True)
            tokenize: "none"            # `tokenize` option in sacrebleu.corpus_bleu() function (options include: "none" (use for already tokenized test data), "13a" (default minimal tokenizer), "intl" which mostly does punctuation and unicode, etc) 

    training:
        #load_model: "{experiment_folder}/models/{name}_transformer/best.ckpt" # if uncommented, load a pre-trained model from this checkpoint
        random_seed: 42
        optimizer: "adam"
        normalization: "tokens"
        adam_betas: [0.9, 0.998] 
        scheduling: "plateau"           
        patience: 7                     
        learning_rate_factor: 0.5       
        learning_rate_warmup: 4000     
        decrease_factor: 0.7
        loss: "crossentropy"
        learning_rate: 0.0003          
        learning_rate_min: 0.00000001
        weight_decay: 0.0
        label_smoothing: 0.1
        batch_size: 4096
        batch_type: "token"
        eval_batch_size: 4096
        eval_batch_type: "token"
        batch_multiplier: 8
        early_stopping_metric: "ppl"
        epochs: 3000                    
        validation_freq: 2500          
        logging_freq: 100
        eval_metric: "bleu"
        model_dir: "{experiment_folder}/models/{name}_transformer"
        overwrite: True              # TODO: Set to True if you want to overwrite possibly existing models. 
        shuffle: True
        use_cuda: True
        fp16: True
        max_output_length: 128
        print_valid_sents: [0, 1, 2, 3]
        keep_last_ckpts: 3

    model:
        initializer: "xavier"
        bias_initializer: "zeros"
        init_gain: 1.0
        embed_initializer: "xavier"
        embed_init_gain: 1.0
        tied_embeddings: True
        tied_softmax: True
        encoder:
            type: "transformer"
            num_layers: 6
            num_heads: 8             
            embeddings:
                embedding_dim: 512   
                scale: True
                dropout: 0.2
            # typically ff_size = 4 x hidden_size
            hidden_size: 512         
            ff_size: 2048            
            dropout: 0.3
        decoder:
            type: "transformer"
            num_layers: 6
            num_heads: 8             
            embeddings:
                embedding_dim: 512    
                scale: True
                dropout: 0.2
            # typically ff_size = 4 x hidden_size
            hidden_size: 512         
            ff_size: 2048           
            dropout: 0.3
    """
    
    with open(f"joeynmt/configs/transformer_{name}.yaml",'w') as f:
        f.write(config)


def clean_up():
    os.system("rm dev.*")
    os.system("rm train.*")
    os.system("rm test.*")
    os.system("rm vocab.*")

    
print("\nstarting to load the data...")

# df = load_data(f"data/train/{source_language}-{target_language}")
# df_dev = load_data(f"data/dev/{source_language}-{target_language}")
# df_test = load_data(f"data/test{source_language}-{target_language}")
# #df_test_ted = load_data(f"data/{source_language}-{target_language}/test/ted")
# #df_test_xwmt = load_data(f"data/{source_language}-{target_language}/test/xwmt")

# print("train samples...")
# print(df.head())
# print("dev samples...")
# print(df_dev.head())
# print("test (bible) samples...")
# print(df_test_bible.head())


# print("\nwriting the tokenized data to files...")
# with open("train."+source_language, "w") as src_file, open("train."+target_language, "w") as trg_file:
#   for index, row in df.iterrows():
#     src_file.write(row["source_sentence"] + "\n")
#     trg_file.write(row["target_sentence"] + "\n")
    
# with open("dev."+source_language, "w") as src_file, open("dev."+target_language, "w") as trg_file:
#   for index, row in df_dev.iterrows():
#     src_file.write(row["source_sentence"] + "\n")
#     trg_file.write(row["target_sentence"] + "\n")
  
# with open("test."+source_language, "w") as src_file, open("test."+target_language, "w") as trg_file:
#   for index, row in df_test_bible.iterrows():
#     src_file.write(row["source_sentence"] + "\n")
#     trg_file.write(row["target_sentence"] + "\n")


print("\nstarting to create BPE splits...")
build_subword_bpe()

build_config()

print("\ncleaning up...")
clean_up()

print("\neverything ready!")




