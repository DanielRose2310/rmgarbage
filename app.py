from clean_heb import clean
import argparse

argParser = argparse.ArgumentParser()

argParser.add_argument("-dir", "--dir")

path = argParser.parse_args()['dir']

