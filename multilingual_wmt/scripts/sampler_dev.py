import os

input_folder = "corpus/dev"
output_folder = "mnmt_bin_dev"

pairs = os.listdir(f"{input_folder}/")


langs = ['alt', 'az', 'ba', 'cjs', 'crh', 'cv', 'gag', 'kaa', 'kjh', 'kk', 'krc', 'kum', 'ky', 'sah', 'slr', 'tk', 'tr', 'tt', 'tyv', 'ug', 'uum', 'uz', 'en', 'ru']


high_pairs = ['en-tr', 'tr-en', 'ru-tr', 'tr-ru', 'uz-ru', 'ru-uz', 'uz-ru', 'kk-ru', 'ru-kk']
medium_pairs = ['az-en', 'en-az', 'az-tr', 'tr-az', 'ba-ru', 'ru-ba', 'kk-en', 'en-kk', 'ky-en', 'en-ky', 'ky-ru', 'ru-ky', 'uz-en', 'en-uz']
low_pairs = ['ba-en', 'en-ba', 'kaa-en', 'en-kaa', 'kaa-uz', 'uz-kaa', 'en-sah', 'sah-en', 'ru-sah', 'sah-ru']

bin_names = ["low", "medium", "high"]

for pair in pairs:
    bin = 0
    if pair in high_pairs:
        bin = 2
    elif pair in medium_pairs:
        bin = 1
    elif pair in low_pairs:
        bin = 0
    else:
        continue
        
    src = pair.split("-")[0]
    tgt = pair.split("-")[1]

    if not os.path.isdir(f"{output_folder}/{bin_names[bin]}"):
        os.makedirs(f"{output_folder}/{bin_names[bin]}")

    src_out = open(f"{output_folder}/{bin_names[bin]}/{bin_names[bin]}.src", "a+")
    tgt_out = open(f"{output_folder}/{bin_names[bin]}/{bin_names[bin]}.tgt", "a+")
    
    dev = open(f"{input_folder}/{pair}/{pair}.{src}").readlines()
    for s in dev:
        src_out.write(f"<2{tgt}> {s}")
    
    dev = open(f"{input_folder}/{pair}/{pair}.{tgt}").readlines()
    for t in dev:
        tgt_out.write(t)

