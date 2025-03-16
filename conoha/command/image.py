from conoha.api import image
from conoha.util.misc import print_json


def image_list():
    print_json(image.list_images())


def image_search(keyword):
    print_json(
        {
            "images": list(
                filter(
                    lambda x: keyword in x.get("name", ""),
                    image.list_images().get("images", []),
                )
            )
        }
    )
