import requests
from assertpy import assert_that
from lxml import etree

from config import COVID_TRACKER_HOST
from utils.print_helpers import pretty_print


def test_covid_cases_have_crossed_a_million():
    response = requests.get(f'{COVID_TRACKER_HOST}/api/v1/summary/latest')
    pretty_print(response.headers)

    response_xml = response.text
    tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
    total_cases = tree.xpath("//data/summary/total_cases")[0].text

    assert_that(int(total_cases)).is_greater_than(1000000)
