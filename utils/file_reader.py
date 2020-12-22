import json
from pathlib import Path

BASE_PATH = Path.cwd().joinpath('..', 'tests', 'data')


def read_file(file_name):
    path = get_file_with_json_extension(file_name)

    with path.open(mode='r') as f:
        return json.load(f)


def get_file_with_json_extension(file_name):
    if '.json' in file_name:
        path = BASE_PATH.joinpath(file_name)
    else:
        path = BASE_PATH.joinpath(f'{file_name}.json')
    return path
