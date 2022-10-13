import uuid
import yaml
import time
import numpy as np
from hashlib import md5
from pathlib import Path
from PIL import Image
from PIL import UnidentifiedImageError


def coord(match=None):
    with open('config_border.yaml', 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)

    config_list, activate = data['border'], data['activate']
    cur_dict = list(filter(lambda x: (x['name'] == activate), config_list))[0]
    result = cur_dict['px']
    if match is not None:
        for key in cur_dict.keys():
            if len(key.split('-')) > 1 and match.lower().find(key[0]) >= 0:
                result = cur_dict[key]
    return tuple(list(map(int, result.split(","))))


def get_config(key):
    with open('config_border.yaml', 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data[key]


def cut(img_path, point):
    origin_im = Image.open(Path(img_path))
    x1, y1, x2, y2 = point
    w, h = origin_im.size
    return origin_im.crop((x1, y1, w - x2, h - y2))


def valid_image(path):
    b_valid = True
    try:
        with open(path, 'rb') as f:
            buf = f.read()
            if buf[6:10] in (b'JFIF', b'Exif'):
                if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                    b_valid = False

        Image.open(path).verify()
    except (UnidentifiedImageError, PermissionError, FileNotFoundError):
        b_valid = False
    return b_valid


def encrypt_md5(s):
    new_md5 = md5()
    new_md5.update(s.encode(encoding='utf-8'))
    return new_md5.hexdigest()


def get_file_licence():
    license_key = ''
    license_path = 'licence.txt'
    if Path(license_path).exists():
        with open(license_path, 'r') as f:
            license_key = f.readline()
    return license_key


def get_sys_licence():
    address = hex(uuid.getnode())[2:]
    return encrypt_md5(address + '_cscsi')


def valid_licence(licence):
    return licence == get_sys_licence()


def spin_im(path):
    # 自旋判断图片完整性，超过 N 秒直接跳过
    sleep_count = 0
    time.sleep(0.5)
    while not valid_image(path) and sleep_count < 8:
        time.sleep(0.5)


def transpose_save(source_path, target_path, height):
    # 水平翻转图像并保存
    print('transpose:', source_path)
    try:
        im = Image.open(source_path).convert('RGB')
        w, h = im.size
        transpose_h = h - height
        Path(target_path).parent.mkdir(parents=True, exist_ok=True)
        im_np = np.array(im)
        im_new_np = np.concatenate((im_np[:transpose_h, ::-1, :], im_np[transpose_h:, :, :]), axis=0)
        Image.fromarray(im_new_np).save(target_path)
    except Exception as err:
        print(err, source_path)
