import random
from json import loads

import pytest
import requests
from assertpy.assertpy import assert_that
from jsonpath_ng import parse

from clients.people.people_client import PeopleClient
from config import BASE_URI
from tests.helpers.people_helpers import search_created_user_in
from utils.file_reader import read_file

client = PeopleClient()


def test_read_all_has_kent():
    response = client.read_all_persons()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.as_dict).extracting('fname').is_not_empty().contains('Kent')


def test_new_person_can_be_added():
    last_name, response = client.create_person()
    peoples = client.read_all_persons().as_dict

    is_new_user_created = search_created_user_in(peoples, last_name)
    assert_that(is_new_user_created).is_not_empty()


def test_created_person_can_be_deleted():
    persons_last_name = client.create_person()

    peoples = client.read_all_persons().as_dict
    new_person_id = search_created_user_in(peoples, persons_last_name)[0]['person_id']

    response = client.delete_person(new_person_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')

    random_no = random.randint(0, 1000)
    last_name = f'Olabini{random_no}'

    payload['lname'] = last_name
    yield payload


def test_person_can_be_added_with_a_json_template(create_data):
    client.create_person(create_data)

    response = requests.get(BASE_URI)
    peoples = loads(response.text)

    # Get all last names for any object in the root array
    # Here $ = root, [*] represents any element in the array
    # Read full syntax: https://pypi.org/project/jsonpath-ng/
    jsonpath_expr = parse("$.[*].lname")
    result = [match.value for match in jsonpath_expr.find(peoples)]
    print(result)

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)
