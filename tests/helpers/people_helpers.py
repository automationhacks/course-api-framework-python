from jsonpath_ng import parse


def search_created_user_in(peoples, last_name):
    return [person for person in peoples if person['lname'] == last_name][0]


def search_nodes_using_json_path(peoples, json_path):
    jsonpath_expr = parse(json_path)
    return [match.value for match in jsonpath_expr.find(peoples)]
