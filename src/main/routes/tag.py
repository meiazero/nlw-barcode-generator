from flask import Blueprint, request, jsonify
from src.dto.http_request import HttpRequest
from src.dto.tag_creator import TagCreator

tag = Blueprint('tag', __name__)


@tag.route('/tag/generate', methods=['POST'])
def generate_tag():
    tag_creator = TagCreator()

    http_request = HttpRequest(body=request.json)
    response = tag_creator.validate_and_create_tag(http_request)

    return jsonify(response.body), response.status_code
