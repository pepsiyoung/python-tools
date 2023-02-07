import json
import os
import argparse
from tqdm import tqdm
from pathlib import Path, PurePath

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
# name2id = {'shaohandai': 0, 'yiwu': 1, 'zhengpian': 2, 'quejiao': 3, 'bingpian': 4}
# name2id = {'SP': 0, 'SC': 1, 'XC': 2, 'PP': 3, 'jLW': 4, 'XH': 5, 'HBN': 6, 'DS': 7, 'HB': 8, 'HS': 9, 'SN': 10}
# name2id = {'txy': 0, 'PP': 1}
# name2id = {'xuhan': 0, 'fanxu': 1, 'liewen': 2, 'duanlu': 3, 'duanshan': 4, 'yiwu': 5, 'quejiao': 6}
name2id = {'xuhan': 0, 'fanxu': 1, 'liewen': 2, 'duanlu': 3, 'quejiao': 4, 'duanshan': 5, 'yiwu': 6}


# name2id = {'binpian': 0, 'bingpian': 0, 'quejiao': 1, "que'jiao": 1, 'shaohandai': 2, 'yiwu': 3, '异物': 3,
#            'zhengpian': 4, 'dajie': 5, 'shouweipian': 6, 'quepian': 7}


def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = abs(box[2] - box[0])
    h = abs(box[3] - box[1])
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_polygon(im_w, im_h, x, y):
    dw = 1. / im_w
    dh = 1. / im_h
    return x * dw, y * dh


def decode_json(opt, json_name):
    # 生成txt文件你想存放的路径
    txt_name = '%s/%s.txt' % (opt.target_dir, json_name[0:-5])
    txt_file = open(txt_name, 'w')

    json_path = os.path.join(opt.source_dir, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:
        label_name = i['label']
        if i['shape_type'] == 'rectangle' and label_name not in opt.ignore:
            x1 = float((i['points'][0][0]))
            y1 = float((i['points'][0][1]))
            x2 = float((i['points'][1][0]))
            y2 = float((i['points'][1][1]))

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')
        elif i['shape_type'] == 'polygon':
            result_xy = []
            for x, y in i['points']:
                normal_x, normal_y = convert_polygon(img_w, img_h, x, y)
                result_xy.append(normal_x)
                result_xy.append(normal_y)
            txt_file.write(f'{str(name2id[label_name])} {" ".join([str(a) for a in result_xy])}\n')
    txt_file.close()


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=str, default=Path(ROOT).joinpath('source'), help='source dir path')
    parser.add_argument('--target-dir', type=str, default=Path(ROOT).joinpath('target'), help='target dir path')
    parser.add_argument('--ignore', nargs='+', type=str, default=[], help='ignore classes')

    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    cur_opt = parse_opt(True)
    json_names = [x for x in Path(cur_opt.source_dir).iterdir() if PurePath(x).match("*.json")]

    for cur_name in tqdm(json_names):
        try:
            decode_json(cur_opt, cur_name.name)
        except KeyError:
            print(f'Error: {cur_name}')
