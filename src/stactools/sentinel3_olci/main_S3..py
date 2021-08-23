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

    input_file = "/Users/williamray/Repositories/sentinel3-olci/tests/test_metadata/xfdumanifest.xml"
    # input_file = "/home/mlamare/Downloads/S1B_EW_GRDM_1SDH_20210813T063842_20210813T063942_028224_035DEE_6523.SAFE"
    output_dir = "/Users/williamray/Repositories/sentinel3-olci/tests/test_metadata/output/"

    item = create_item_command(input_file, output_dir)

    print(item)