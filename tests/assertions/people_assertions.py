from assertpy import assert_that


def assert_people_have_person_with_first_name(response, first_name):
    assert_that(response.as_dict).extracting('fname').is_not_empty().contains(first_name)


def assert_person_is_present(is_new_user_created):
    assert_that(is_new_user_created).is_not_empty()
