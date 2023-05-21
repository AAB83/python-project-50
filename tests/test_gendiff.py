import pytest
from gendiff import generate_diff


def test_generate_diff_1():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    result = open('tests/fixtures/result_1.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result


def test_generate_diff_2():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file3.json'
    result = open('tests/fixtures/result_2.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result


def test_generate_diff_3():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file4.json'
    result = open('tests/fixtures/result_3.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result
