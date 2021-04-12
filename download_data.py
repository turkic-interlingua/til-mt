import sys
import requests
import zipfile
import os
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

if __name__ == "__main__":

    
    source = sys.argv[1]
    target = sys.argv[2]
    # check if the language code exists in the corpus
    if source not in langs or target not in langs:
        print("Language code error!!!\nLanguage code must be one of these: ")
        print(langs)
        quit()
    
    # create the needed folders if they don't exist already
    if not os.path.isdir(f"data/{source}-{target}"):
        os.mkdir(f"data/{source}-{target}")
        os.mkdir(f"data/{source}-{target}/train")
        os.mkdir(f"data/{source}-{target}/dev")
        os.mkdir(f"data/{source}-{target}/test")
        os.mkdir(f"data/{source}-{target}/test/bible")
        os.mkdir(f"data/{source}-{target}/test/ted")
        os.mkdir(f"data/{source}-{target}/test/x-wmt")
    
    # base save path
    save_path = f"data/{source}-{target}/"

    # these define where to find the needed zip file in the remote host
    train_path = f"{base_url}/train/{source}-{target}"
    dev_path = f"{base_url}/dev/{source}-{target}"
    test_bible_path = f"{base_url}/test/bible/{source}-{target}"
    test_ted_path = f"{base_url}/test/ted/{source}-{target}"
    test_x_wmt_path = f"{base_url}/test/x-wmt/{source}-{target}"

    # download all the needed data
    print("Downloading train files...")
    download_url(train_path, save_path + f"train/")
    
    print("Downloading dev files...")
    download_url(dev_path, save_path + f"dev/")

    print("Downloading bible test files...")
    download_url(test_bible_path, save_path + f"test/bible/")
    
    print("Downloading ted talk test files...")
    download_url(test_ted_path, save_path + f"test/ted/")
    
    print("Downloading x-wmt test files...")
    download_url(test_x_wmt_path, save_path + f"test/x-wmt/")
    
    # # unzip all the data
    # print("Unzipping...")
    # unzip(f"data/{source}-{target}/train/{source}-{target}.zip", f"data/{source}-{target}/train/{source}-{target}")

    # unzip(f"data/{source}-{target}/dev/{source}-{target}.zip", f"data/{source}-{target}/dev/{source}-{target}")

    # unzip(f"data/{source}-{target}/test/bible/{source}-{target}.zip", f"data/{source}-{target}/test/bible/{source}-{target}")
    # unzip(f"data/{source}-{target}/test/ted/{source}-{target}.zip", f"data/{source}-{target}/test/ted/{source}-{target}")
    # unzip(f"data/{source}-{target}/test/x-wmt/{source}-{target}.zip", f"data/{source}-{target}/test/x-wmt/{source}-{target}")

    # # remove the zip files after the unzip is done
    # print("Removing zip files...")
    # os.system(f"rm data/{source}-{target}/train/{source}-{target}.zip")
    # os.system(f"rm data/{source}-{target}/dev/{source}-{target}.zip")
    # os.system(f"rm data/{source}-{target}/test/bible/{source}-{target}.zip")
    # os.system(f"rm data/{source}-{target}/test/ted/{source}-{target}.zip")
    # os.system(f"rm data/{source}-{target}/test/x-wmt/{source}-{target}.zip")


    




    

    