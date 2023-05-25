import json
import yaml
from yaml import SafeLoader
from gendiff.parser import gendiff_args


def generate_diff(file_path1, file_path2):
    diff = []
    if file_path1.split('.')[1] == 'json':
        file_1 = json.load(open(file_path1))
        file_2 = json.load(open(file_path2))
    elif file_path1.split('.')[1] in ('yaml', 'yml'):
        file_1 = yaml.load(open(file_path1), Loader=SafeLoader)
        file_2 = yaml.load(open(file_path2), Loader=SafeLoader)
    else:
        raise Exception('Invalid file format')

    key_set_file1 = set(file_1.keys())
    key_set_file2 = set(file_2.keys())

    key_remote = key_set_file1 - key_set_file2
    key_add = key_set_file2 - key_set_file1
    key_same = key_set_file1 & key_set_file2

    diff += list(map(lambda item: f'  - {item}: {file_1[item]}', key_remote))
    diff += list(map(lambda item: f'  + {item}: {file_2[item]}', key_add))
    for item in key_same:
        if file_1[item] == file_2[item]:
            diff.append(f'    {item}: {file_1[item]}')
        else:
            diff.append(f'  - {item}: {file_1[item]}')
            diff.append(f'  + {item}: {file_2[item]}')
    diff.sort(key=lambda item: item[4:item.find(':')])
    diff = ['{'] + diff + ['}']
    return '\n'.join(diff)


def gendiff():
    file_path1, file_path2 = gendiff_args()
    diff = generate_diff(file_path1, file_path2)
    print(diff)
