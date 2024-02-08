from flask import Blueprint, request, jsonify
from src.dto.http_request import HttpRequest
from src.dto.tag_creator import TagCreator

from src.errors.error_handler import handle_errors

from src.validators.tag_creator import tag_creator_validator

tag = Blueprint('tag', __name__)


@tag.route('/tag/generate', methods=['POST'])
def generate_tag():
    response = None

    try:
        tag_creator_validator(request)
        tag_creator = TagCreator()

        http_request = HttpRequest(body=request.json)
        response = tag_creator.validate_and_create_tag(http_request)
    except Exception as error:
        response = handle_errors(error)

    return jsonify(response.body), response.status_code
