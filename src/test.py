import os
from os import listdir, getcwd
from pathlib import Path, PurePath

# out_file = open(' ./labels/' + 'www.' + 'txt', 'w')
# f = open('./labels/www.txt', 'w')
wd = getcwd()
print('wd=', wd)
print('os_file=', os.path.abspath(__file__))

print('resolve=', Path('.').resolve())
