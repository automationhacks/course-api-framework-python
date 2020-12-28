from json import dumps
from uuid import uuid4

import requests
from assertpy import assert_that

from config import BASE_URI
from utils.request import get, post


class PeopleClient:
    def __init__(self):
        self.base_url = BASE_URI

    def create_person(self, body=None):
        last_name, response = self.create_person_with_unique_last_name(body)
        assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)
        return last_name, response

    def read_one_person_by_id(self, person_id):
        pass

    def read_all_persons(self):
        return get(self.base_url)

    def update_person(self):
        pass

    def delete_person(self, person_id):
        delete_url = f'{BASE_URI}/{person_id}'


    def create_person_with_unique_last_name(self, body=None):
        if body is None:
            last_name = f'User {str(uuid4())}'
            payload = dumps({
                'fname': 'New',
                'lname': last_name
            })
        else:
            last_name = body['lname']
            payload = dumps(body)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = post(self.base_url, payload, headers)
        return last_name, response
