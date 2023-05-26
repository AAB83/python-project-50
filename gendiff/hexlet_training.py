DATA = {"hello": "world", "is": True, "nested": {"count": 5}}
DATA_FLAT = {"hello": "world", "is": True, "nested": 125}
VALUE = True


def stringify(value, char=' ', space=1):
    if type(value) in (int, str, bool):
        return str(value)

    result = list(map(lambda item: f'{char * space}{item}: {stringify(value[item], char, space)}', value))
    result = ['{'] + result + ['}']
    return '\n'.join(result)


test = stringify(DATA)
print(test)
