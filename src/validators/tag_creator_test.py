from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator import tag_creator_validator


class MockRequest:
    def __init__(self, json):
        self.json = json


def test_tag_creator_validator():
    request = MockRequest({
        "product_code": "12345"
    })

    assert tag_creator_validator(request) is None


def test_tag_creator_validator_with_error():
    request = MockRequest({
        "product_code": ""
    })

    try:
        tag_creator_validator(request)
    except Exception as error:
        assert isinstance(error, HttpUnprocessableEntityError)
