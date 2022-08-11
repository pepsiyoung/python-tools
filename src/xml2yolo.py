import xml.etree.ElementTree as elementTree
import argparse
from tqdm import tqdm
from pathlib import Path


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--classes', nargs='+', type=str, default=['xuhan', 'liepian', 'duanlu'])
    parser.add_argument('--source', type=str, default='./source')
    parser.add_argument('--target', type=str, default='./target')
    return parser.parse_known_args()[0] if known else parser.parse_args()


def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = abs(box[1] - box[0])
    h = abs(box[3] - box[2])

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(source_path):
    classes = opt.classes
    in_file = open(source_path)
    out_file = open('{}/{}.txt'.format(opt.target, source_path.stem), 'w')
    tree = elementTree.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == "__main__":
    opt = parse_opt(True)
    xml_paths = Path(opt.source).glob('**/*.xml')
    for xml_path in tqdm(list(xml_paths)):
        convert_annotation(xml_path)
