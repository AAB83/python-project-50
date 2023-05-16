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
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))
    print(f'{file_1}, {type(file_1)=}')
    print(f'{file_2}, {type(file_2)=}')


def gendiff():
    file_path1, file_path2 = gendiff_args()
    generate_diff(file_path1, file_path2)
