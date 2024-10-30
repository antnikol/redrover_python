from http.client import responses

from lesson1.api_tests.case.pom.case import get_root
from lesson1.api_tests.case.models.case import Case
from lesson1.api_tests.case.data.case import create_case_dict
import lesson1.api_tests.utils.api_response
from requests import request

def test_read_test_case_by_id():
    response = request("GET",'http://127.0.0.1:8000/testcases/1'
    assert response.status_code == 200