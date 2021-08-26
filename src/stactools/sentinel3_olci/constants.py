
import pystac
from pystac.link import Link

from pystac.extensions.eo import Band

INSPIRE_METADATA_ASSET_KEY = "inspire-metadata"
SAFE_MANIFEST_ASSET_KEY = "safe-manifest"
PRODUCT_METADATA_ASSET_KEY = "product-metadata"

SENTINEL_LICENSE = Link(
    rel="license",
    target="https://sentinel.esa.int/documents/"
    + "247904/690755/Sentinel_Data_Legal_Notice",
)

PRODUCT_TYPE = "OLCI"

#NOT SURE BEST NAME FOR OLCI PRODUCT TYPE

SENTINEL_CONSTELLATION = "Sentinel 1"

SENTINEL_PROVIDER = pystac.Provider(
    name="ESA",
    roles=["producer", "processor", "licensor"],
    url="https://earth.esa.int/web/guest/home",
)

SAFE_MANIFEST_ASSET_KEY = "safe-manifest"


