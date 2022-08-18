import uuid
import yaml
from hashlib import md5
from pathlib import Path
from PIL import Image
from PIL import UnidentifiedImageError


def coord():
    with open('config_border.yaml', 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)

    config_list, activate = data['border'], data['activate']
    res = list(filter(lambda x: (x['name'] == activate), config_list))[0]['px']
    return tuple(list(map(int, res.split(","))))


def cut(img_path, point):
    origin_im = Image.open(Path(img_path))
    x1, y1, x2, y2 = point
    w, h = origin_im.size
    return origin_im.crop((x1, y1, w - x2, h - y2))


def valid_image(path):
    b_valid = True
    try:
        Image.open(path).verify()
    except (UnidentifiedImageError, PermissionError):
        b_valid = False
    print('b_valid:', b_valid)
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
