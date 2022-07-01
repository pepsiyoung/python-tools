import json
import os
import argparse
from tqdm import tqdm
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
name2id = {'person': 0, 'hook': 1}


def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def decode_json(opt, json_name):
    # 生成txt文件你想存放的路径
    # txt_name = opt.target_folder + json_name[0:-5] + '.txt'
    txt_name = '%s/%s.txt' % (opt.target_folder, json_name[0:-5])
    txt_file = open(txt_name, 'w')

    json_path = os.path.join(opt.source_folder, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:
        label_name = i['label']
        if i['shape_type'] == 'rectangle':
            x1 = float((i['points'][0][0]))
            y1 = float((i['points'][0][1]))
            x2 = float((i['points'][1][0]))
            y2 = float((i['points'][1][1]))

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-folder', type=str, default=Path(ROOT).joinpath('source'), help='source folder path')
    parser.add_argument('--target-folder', type=str, default=Path(ROOT).joinpath('target'), help='target folder path')

    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    # json_names = os.listdir(opt.source_folder)
    json_names = Path(opt.source_folder).glob("**/*.jpg")

    for json_name in tqdm(json_names):
        # txt_name = '%s/%s.txt' % (opt.target_folder, json_name[0:-5])
        # txt_file = open(txt_name, 'w')
        decode_json(opt, json_name)
        # print(json_name)
