import sys
import requests
import zipfile
import os
import argparse

base_url = "gs://til-corpus/corpus"

# all the langs present in the corpus
langs = ['alt', 'az', 'ba', 'cjs', 'crh', 'cv', 'gag', 'kaa', 'kjh', 'kk', 'krc', 'kum', 'ky', 'sah', 'slr', 'tk', 'tr', 'tt', 'tyv', 'ug', 'uum', 'uz', 'en', 'ru']

# downloads a zip file given a url
def download_url(url, save_path):
    try:
        os.system(f"gsutil -m cp -r {url} {save_path}")
    except CommandException as e:
        print("Requested test files are not found!")
    

def unzip(path_to_zip_file, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

def create_folder(source, target, split):

    if not os.path.isdir(f"data/{source}-{target}/{split}"):
        os.makedirs(f"data/{source}-{target}/{split}")
    
    



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--source_language', default=None, type=str, required=True,
        help='2-letter code of the source language')
    parser.add_argument('--target_language', default=None, type=str, required=True,
        help='2-letter code of the target language')
    parser.add_argument('--split', default="all", type=str, required=False,
        help='which split to download. Options: \{"train", "dev", "test"\}')
    args = parser.parse_args()
    
    source = args.source_language
    target = args.target_language
    
    # check if the language code exists in the corpus
    if source not in langs or target not in langs:
        print("Language code error!!!\nLanguage code must be one of these: ")
        print(langs)
        quit()
    
    
    if args.split not in ["train", "dev", "test", "all"]:
        print("Splits should be one of the following: [train, dev, test, all]")
        quit()

    
    splits = ["train", "dev", "test"] if args.split == "all" else [args.split]

    for split in splits:
        create_folder(source, target, split)

        
        # base save path
        save_path = f"data/{source}-{target}/"

        if split == "test":
            create_folder(source, target, split + "/bible")
            create_folder(source, target, split + "/ted")
            create_folder(source, target, split + "/x-wmt")
        
            test_bible_path = f"{base_url}/test/bible/{source}-{target}"
            test_ted_path = f"{base_url}/test/ted/{source}-{target}"
            test_x_wmt_path = f"{base_url}/test/x-wmt/{source}-{target}"

            print("Downloading bible test files...")
            download_url(test_bible_path, save_path + f"test/bible/")
    
            print("Downloading ted talk test files...")
            download_url(test_ted_path, save_path + f"test/ted/")
    
            print("Downloading x-wmt test files...")
            download_url(test_x_wmt_path, save_path + f"test/x-wmt/")
    
        else:

            download_path = f"{base_url}/{split}/{source}-{target}"
            print(f"Downloading {split} files...")
            download_url(download_path, save_path + f"{split}/")

 

    




    

    