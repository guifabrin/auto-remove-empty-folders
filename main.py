import os
from dotenv import dotenv_values

config = dotenv_values('.env')


def remove_empty_folders(path_abs):
    try:
        items = os.listdir(path_abs)
    except:
        return 0
    if len(items) == 0:
        os.removedirs(path_abs)
        return 1
    count = 0
    for item in items:
        if os.path.isdir(path_abs + item + '\\'):
            count += remove_empty_folders(path_abs + item + '\\')
    return count


if __name__ == '__main__':
    while True:
        if remove_empty_folders(config['PATH']) == 0:
            break
