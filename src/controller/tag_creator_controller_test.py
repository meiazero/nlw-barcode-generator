from unittest.mock import patch
from src.driver.barcode import BarCodeHandler
from .tag_creator_controlller import TagCreatorController


@patch.object(BarCodeHandler, "create_bar_code", )
def test_create_tag(mock_create_bar_code):
    mock_values = {
        "product_code": "234523-4234-234-234",
    }
    mock_create_bar_code.return_value = f'tags/{mock_values["product_code"]}'

    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_values["product_code"])

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] is not None
    assert result["data"]["path"] == f'tags/{mock_values["product_code"]}.png'
