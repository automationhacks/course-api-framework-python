import requests

from clients.people.people_client import PeopleClient
from tests.assertions.people_assertions import *
from tests.helpers.people_helpers import *

client = PeopleClient()


def test_read_all_has_kent(logger):
    """
    Verify people API database GET operation returns a user with first name as kent
    :param logger:
    :return:
    """
    response = client.read_all_persons()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    logger.info("User successfully read")
    assert_people_have_person_with_first_name(response, first_name='Kent')


def test_new_person_can_be_added():
    last_name, response = client.create_person()
    assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)

    peoples = client.read_all_persons().as_dict
    is_new_user_created = search_created_user_in(peoples, last_name)
    assert_person_is_present(is_new_user_created)


def test_created_person_can_be_deleted():
    persons_last_name, _ = client.create_person()

    peoples = client.read_all_persons().as_dict
    new_person_id = search_created_user_in(peoples, persons_last_name)['person_id']

    response = client.delete_person(new_person_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_person_can_be_added_with_a_json_template(create_data):
    client.create_person(create_data)

    response = client.read_all_persons()
    peoples = response.as_dict

    result = search_nodes_using_json_path(peoples, json_path="$.[*].lname")

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)
