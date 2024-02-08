import os

from barcode import Code128
from barcode.writer import ImageWriter


class BarCodeHandler:
    def create_bar_code(self: object, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())

        # change to a better place to save the tag
        path_to_save_tag = os.path.join('tags', product_code)
        tag.save(path_to_save_tag)

        return path_to_save_tag
