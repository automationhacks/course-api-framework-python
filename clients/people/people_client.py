from json import dumps
from uuid import uuid4

from clients.people.base_client import BaseClient
from config import BASE_URI
from utils.request import APIRequest


class PeopleClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_person(self, body=None):
        last_name, response = self.__create_person_with_unique_last_name(body)
        return last_name, response

    def __create_person_with_unique_last_name(self, body=None):
        if body is None:
            last_name = f'User {str(uuid4())}'
            payload = dumps({
                'fname': 'New',
                'lname': last_name
            })
        else:
            last_name = body['lname']
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)
        return last_name, response

    def read_one_person_by_id(self, person_id):
        pass

    def read_all_persons(self):
        return self.request.get(self.base_url)

    def update_person(self):
        pass

    def delete_person(self, person_id):
        url = f'{BASE_URI}/{person_id}'
        return self.request.delete(url)
