from my_utils import get_sys_licence

if __name__ == '__main__':
    with open('licence.txt', 'w') as f:
        f.write(get_sys_licence())
