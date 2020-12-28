from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


def __get_responses(response):
    status_code = response.status_code
    text = response.text

    try:
        as_dict = response.json()
    except Exception:
        as_dict = {}

    headers = response.headers

    return Response(
        status_code, text, as_dict, headers
    )


def get(url):
    response = requests.get(url)
    return __get_responses(response)


def post(url, payload, headers):
    response = requests.post(url, data=payload, headers=headers)
    return __get_responses(response)


def delete(url):
    response = requests.delete(url)
    return __get_responses(response)
