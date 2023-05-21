import pytest
from gendiff import generate_diff


@pytest.fixture()
def data_1():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    return file_path1, file_path2


@pytest.fixture()
def data_2():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file3.json'
    return file_path1, file_path2


@pytest.fixture()
def data_3():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file4.json'
    return file_path1, file_path2


def test_generate_diff_1(data_1):
    file_path1, file_path2 = data_1
    result = open('tests/fixtures/result_1.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result


def test_generate_diff_2(data_2):
    file_path1, file_path2 = data_2
    result = open('tests/fixtures/result_2.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result


def test_generate_diff_3(data_3):
    file_path1, file_path2 = data_3
    result = open('tests/fixtures/result_3.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result
