from stactools.core.io.xml import XmlElement


def fill_sat_properties(sat_ext, href):
    """Fills the properties for SAR.
    Based on the sar Extension.py
    Args:
        input_ext (pystac.extensions.sar.SarExtension): The extension to be populated.
        href (str): The HREF to the scene, this is expected to be an XML file.
    Returns:
        pystac.Asset: An asset with the SAR relevant properties.
    """
    # Read meta file
    root = XmlElement.from_file(href)

    sat_ext.platform_international_designator = root.findall(
        ".//safe:nssdcIdentifier")[0].text

    orbit_state = root.findall(".//s1:pass")[0].text
    sat_ext.orbit_state = OrbitState(orbit_state.lower())

    sat_ext.absolute_orbit = int(root.findall(".//safe:orbitNumber")[0].text)

    sat_ext.relative_orbit = int(
        root.findall(".//safe:relativeOrbitNumber")[0].text)


def fill_proj_properties(proj_ext, meta_links, product_meta):
    """Fills the properties for SAR.
    Based on the sar Extension.py
    Args:
        input_ext (pystac.extensions.sar.SarExtension): The extension to be populated.
        href (str): The HREF to the scene, this is expected to be an XML file.
    Returns:
        pystac.Asset: An asset with the SAR relevant properties.
    """
    # Read meta file
    links = meta_links.create_product_asset()
    root = XmlElement.from_file(links[0][1].href)

    proj_ext.epsg = 4326

    proj_ext.geometry = product_meta.geometry

    proj_ext.bbox = product_meta.bbox

    x_size = int(root.findall(".//numberOfSamples")[0].text)
    y_size = int(root.findall(".//numberOfLines")[0].text)

    proj_ext.shape = [x_size, y_size]