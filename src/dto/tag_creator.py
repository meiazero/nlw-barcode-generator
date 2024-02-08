from src.dto.http_request import HttpRequest
from src.dto.http_response import HttpResponse

from src.controller.tag_creator_controlller import TagCreatorController


class TagCreator:

    def validate_and_create_tag(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["product_code"]

        #  regras de negócio
        tag = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=201, body=tag)
