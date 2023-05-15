import pytest
from gendiff_package.gendiff_main import generate_diff


@pytest.fixture()
def data():
    file_path1 = 'tests/data/file1.json'
    file_path2 = 'tests/data/file2.json'
    return file_path1, file_path2


def test_generate_diff(data):
    file_path1, file_path2 = data
    diff = generate_diff(file_path1, file_path2)
    result = '- follow: false\nhost: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true'
    assert diff == result
