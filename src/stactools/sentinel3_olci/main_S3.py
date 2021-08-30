import os
import sys

from stac import create_item


def create_item_command(src, dst):
    """Creates a STAC Collection
    Args:
        src (str): path to the scene
        dst (str): path to the STAC Item JSON file that will be created
    """
    item = create_item(src)

    item_path = os.path.join(dst, "{}.json".format(item.id))
    item.set_self_href(item_path)

    item.save_object()

    return item


if __name__ == "__main__":

    input_file = "/Users/williamray/Repositories/sentinel3-olci/tests/test_metadata/S3A_OL_1_EFR____20210820T103153_20210820T103453_20210820T124206_0179_075_222_2160_LN1_O_NR_002.SEN3/xfdumanifest.xml"
    output_dir = "/Users/williamray/Repositories/sentinel3-olci/tests/test_metadata/output/"

    item = create_item_command(input_file, output_dir)

    print(item)