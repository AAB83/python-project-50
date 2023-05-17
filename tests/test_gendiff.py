import pytest
from gendiff import generate_diff


@pytest.fixture()
def data():
    file_path1 = 'fixtures/file1.json'
    file_path2 = 'fixtures/file2.json'
    return file_path1, file_path2


def test_generate_diff(data):
    file_path1, file_path2 = data
    result = open('fixtures/result_1.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result
