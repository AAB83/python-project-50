import argparse
import json


def gendiff_args():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                                 ' files and shows'
                                                 ' a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='FORMAT',
                        help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def generate_diff(file_path1, file_path2):
    diff = []
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))

    key_set_file1 = set(file_1.keys())
    key_set_file2 = set(file_2.keys())

    key_remote = key_set_file1 - key_set_file2
    key_add = key_set_file2 - key_set_file1
    key_same = key_set_file1 & key_set_file2

    diff += list(map(lambda item: f'  - {item}:{file_1[item]}', key_remote))
    diff += list(map(lambda item: f'  + {item}:{file_2[item]}', key_add))
    for item in key_same:
        if file_1[item] == file_2[item]:
            diff.append(f'    {item}:{file_1[item]}')
        else:
            diff.append(f'  - {item}:{file_1[item]}')
            diff.append(f'  + {item}:{file_2[item]}')
    diff = ['{'] + diff
    diff.append('}')
    return '\n'.join(diff)


def gendiff():
    file_path1, file_path2 = gendiff_args()
    diff = generate_diff(file_path1, file_path2)
    print(diff)
