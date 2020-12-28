def search_created_user_in(peoples, last_name):
    return [person for person in peoples if person['lname'] == last_name]