import requests
from assertpy.assertpy import assert_that

from json import dumps
from config import BASE_URI
from utils.print_helpers import pretty_print
from uuid import uuid4


def test_read_all_has_kent():
    response = requests.get(BASE_URI)
    response_text = response.json()
    pretty_print(response_text)

    assert_that(response.status_code).is_equal_to(200)
    first_names = [people['fname'] for people in response_text]
    assert_that(first_names).contains('Kent')


def test_new_person_can_be_added():
    unique_last_name = f'User {str(uuid4())}'
    payload = dumps({
        'fname': 'New',
        'lname': unique_last_name
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(204)

    people = requests.get(BASE_URI).json()
    is_new_user_created = filter(lambda person: person['lname'] == unique_last_name, people)
    assert_that(is_new_user_created).is_true()
