import json
import os
import argparse
from tqdm import tqdm
from pathlib import Path, PurePath

if __name__ == "__main__":
    image_paths = [x for x in Path('./images').iterdir() if PurePath(x).match("*.jpg")]
    for image_path in tqdm(image_paths):
        image_name = image_path.stem

        try:
            in_file = open('./annotations/{}.xml'.format(image_name))
        except FileNotFoundError as e:
            print(e)
