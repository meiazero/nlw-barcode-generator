from typing import Dict
from src.driver.barcode import BarCodeHandler


# noinspection PyArgumentList
class TagCreatorController:

    def create(self, product_code: str) -> Dict:
        path_to_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_to_tag)

        return formatted_response


    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarCodeHandler()
        path_to_tag = barcode_handler.create_bar_code(product_code)

        return path_to_tag


    def __format_response(self, path_to_tag: str, count: int = 1) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": count,
                "path": f'{path_to_tag}.png'
            }
        }
