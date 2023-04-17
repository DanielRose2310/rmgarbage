from clean_heb import clean_text
import argparse
from glob import glob
from tqdm import tqdm

argParser = argparse.ArgumentParser()

argParser.add_argument("-path", "--path")

path = argParser.parse_args().path

if '__parsed__' in path:
    files = glob(path+'*')
    for file in tqdm(files):
        if '.txt' in file:
            txt = open(file,mode='r',encoding='utf-8').read()
            cleaned_txt = clean_text(txt)
            with open(file.replace('__parsed__','__cleaned__'),mode='w',encoding='utf-8') as f:
                f.write(cleaned_txt)