import os
import csv
import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

corpus_folder = "corpus"

langs = ['alt', 'az', 'ba', 'crh', 'cv', 'gag', 'kaa', 'kjh', 'kk', 'krc', 'kum', 'ky', 'sah', 'tk', 'tr', 'tt', 'tyv', 'ug', 'uz', 'en', 'ru']

pair_size = {}

def get_proportions():
    
    total = 0
    all_pairs = os.listdir(f"{corpus_folder}/train")
    for pair in all_pairs:
        src = pair.split("-")[0]
        tgt = pair.split("-")[1]
        if src in langs and tgt in langs:
            with open(f"{corpus_folder}/train/{pair}/{pair}.{src}") as f:
                count = sum(1 for _ in f)
            
            pair_size[pair] = count
            total += count
    
    return total


def get_temp_ratios(args, total):
    # formula goes like = [(x / total_size) ** (1.0 / temperature) for x in pair_size]

    ratios = {}
    new_total = 0
    for key, value in pair_size.items():
        ratios[key] = int((value / total) ** (1.0 / args.temp) * total)
        new_total += ratios[key]

    return ratios, new_total    


def load_dev_test(args):
    dev_test = []

    pairs = os.listdir(f"corpus/dev/")

    for pair in pairs:
        src = pair.split("-")[0]
        tgt = pair.split("-")[1]
        if src in langs and tgt in langs:
            dev_test += open(f"corpus/dev/{pair}/{pair}.{src}").readlines()
            dev_test += open(f"corpus/dev/{pair}/{pair}.{tgt}").readlines()

            dev_test += open(f"corpus/test/{pair}/{pair}.{src}").readlines()
            dev_test += open(f"corpus/test/{pair}/{pair}.{tgt}").readlines()
    
    return set(dev_test)

def sample(args, pair, size, sample_amount, dev_test):
    
    multiplier = int(sample_amount/size)
    remainder = sample_amount % size

    src = pair.split("-")[0]
    tgt = pair.split("-")[1]

    src_out = open("multilingual.src", "a")
    tgt_out = open("multilingual.tgt", "a")
    with open(f"{args.input_folder}/{pair}/{pair}.{src}", "r") as source, open(f"{args.input_folder}/{pair}/{pair}.{tgt}", "r") as target:
        for s, t in zip(source, target):
            if s not in dev_test and t not in dev_test:
                for i in range(multiplier):
                    src_out.write(f"<2{tgt}> {s}")
                    tgt_out.write(t)
        
    with open(f"{args.input_folder}/{pair}/{pair}.{src}", "r") as source, open(f"{args.input_folder}/{pair}/{pair}.{tgt}", "r") as target:
        count = 0
        for s, t in zip(source, target):

            if count > remainder:
                break
            
            if s not in dev_test and t not in dev_test:
                src_out.write(f"<2{tgt}> {s}")
                tgt_out.write(t)
                count += 1
    
    src_out.close()
    tgt_out.close()



if __name__ == "__main__":
    import  argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input_folder', required=True, type=str,  help='input folder where all the parallel data exist')
    #parser.add_argument('--output_folder', required=True, type=str, help='output folder with the resampled data')
    parser.add_argument('--temp', required=True, type=float, help='temperature for the sampling')
    
    logs = open("logs.txt", "w")
    args = parser.parse_args()
    
    total = get_proportions()

    print(total)

    new_ratios, new_total = get_temp_ratios(args, total)

    print(new_total)

    dev_test = load_dev_test(args)

    print(len(dev_test))

    for key, value in new_ratios.items():
        print(f"{key} : {pair_size[key]}  -->  {value}")
        logs.write(f"{key}\t{pair_size[key]}\t{value}\n")
        sample(args, key, pair_size[key], value, dev_test)

    




    




    




