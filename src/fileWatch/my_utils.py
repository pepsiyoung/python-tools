import uuid
from hashlib import md5
from pathlib import Path


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
