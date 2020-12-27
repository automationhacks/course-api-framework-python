import json

import requests
from cerberus import Validator

from config import BASE_URI


def test_read_all_operation_has_expected_schema():
    schema = {
        "fname": {'type': 'string'},
        "lname": {'type': 'string'},
        "person_id": {'type': 'integer'},
        "timestamp": {'type': 'string'}
    }

    response = requests.get(BASE_URI)
    persons = json.loads(response.text)

    validator = Validator(schema)

    for person in persons:
        is_valid = validator.validate(person)

        if not is_valid:
            print(validator.errors)
