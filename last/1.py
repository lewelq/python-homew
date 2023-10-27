import os
import logging
from collections import namedtuple

logging.basicConfig(filename='file_info.log', level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])

def get_file_info(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        is_dir = os.path.isdir(full_path)
        parent_dir = os.path.basename(os.path.dirname(full_path))
        if is_dir:
            name = item
            extension = ''
        else:
            name, extension = os.path.splitext(item)
        file_info = FileInfo(name, extension, is_dir, parent_dir)
        logging.info(file_info)
        print(file_info)

if __name__ == '__main__':
    path = input('Enter directory path: ')
    get_file_info(path)