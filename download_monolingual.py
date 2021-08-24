import sys
import requests
import zipfile
import os
import argparse

base_url = "gs://til-corpus/mono"

# all the langs present in the corpus
langs = ['alt', 'az', 'ba', 'cjs', 'crh', 'cv', 'gag', 'kaa', 'kjh', 'kk', 'krc', 'kum', 'ky', 'sah', 'slr', 'tk', 'tr', 'tt', 'tyv', 'ug', 'uum', 'uz', 'en', 'ru']

# downloads a zip file given a url
def download_url(url, save_path):
    try:
        os.system(f"gsutil -m cp -r {url} {save_path}")
    except CommandException as e:
        print("Requested test files are not found!")
        
    



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--language', default=None, type=str, required=True,
        help='2-letter code of the source language')
    
    args = parser.parse_args()
    
    language = args.language
    
    
    # check if the language code exists in the corpus
    if language not in langs:
        print("Language code error!!!\nLanguage code must be one of these: ")
        print(langs)
        quit()
    
    download_url(f"{base_url}/{language}.txt", f"monolingual/{language}.txt")
    
    

 

    




    

    