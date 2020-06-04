"""Functions to translate entire Ladybug core objects to Rhino geometries.

The methods here are intended to help translate groups of geometry that are commonly
generated by several objects in Ladybug core (ie. legends, compasses, etc.)
"""

from .fromgeometry import from_mesh3d, from_arc2d, from_linesegment2d
from .text import text_objects

try:
    from ladybug_geometry.geometry3d.pointvector import Point3D
    from ladybug_geometry.geometry3d.plane import Plane
except ImportError as e:
    raise ImportError("Failed to import ladybug_geometry.\n{}".format(e))


def legend_objects(legend):
    """Translate a Ladybug Legend object into Grasshopper geometry.

    Args:
        legend: A Ladybug Legend object to be converted to Rhino geometry.

    Returns:
        A list of Rhino geometries in the following order.

        -   legend_mesh -- A colored mesh for the legend.

        -   legend_title -- A bake-able text object for the legend title.

        -   legend_text -- Bake-able text objects for the rest of the legend text.
    """
    _height = legend.legend_parameters.text_height
    _font = legend.legend_parameters.font
    legend_mesh = from_mesh3d(legend.segment_mesh)
    legend_title = text_objects(legend.title, legend.title_location, _height, _font)
    if legend.legend_parameters.continuous_legend is False:
        legend_text = [text_objects(txt, loc, _height, _font, 0, 5) for txt, loc in
                       zip(legend.segment_text, legend.segment_text_location)]
    elif legend.legend_parameters.vertical is True:
        legend_text = [text_objects(txt, loc, _height, _font, 0, 3) for txt, loc in
                       zip(legend.segment_text, legend.segment_text_location)]
    else:
        legend_text = [text_objects(txt, loc, _height, _font, 1, 5) for txt, loc in
                       zip(legend.segment_text, legend.segment_text_location)]
    return [legend_mesh] + [legend_title] + legend_text


def compass_objects(compass, z=0, custom_angles=None, projection=None, font='Arial'):
    """Translate a Ladybug Compass object into Grasshopper geometry.

    Args:
        compass: A Ladybug Compass object to be converted to Rhino geometry.
        z: A number for the Z-coordinate to be used in translation. (Default: 0)
        custom_angles: An array of numbers between 0 and 360 to be used to
            generate custom angle labels around the compass.
        projection: Text for the name of the projection to use from the sky
            dome hemisphere to the 2D plane. If None, no altitude circles o
            labels will be drawn (Default: None). Choose from the following:

                * Orthographic
                * Stereographic

        font: Optional text for the font to be used in creating the text.
            (Default: 'Arial')

    Returns:
        A list of Rhino geometries in the following order.

        -   all_boundary_circles -- Three Circle objects for the compass boundary.

        -   major_azimuth_ticks -- Line objects for the major azimuth labels.

        -   major_azimuth_text -- Bake-able text objects for the major azimuth labels.

        -   minor_azimuth_ticks -- Line objects for the minor azimuth labels
                (if applicable).

        -   minor_azimuth_text -- Bake-able text objects for the minor azimuth
                labels (if applicable).

        -   altitude_circles -- Circle objects for the altitude labels.

        -   altitude_text -- Bake-able text objects for the altitude labels.

     """
    # set default variables based on the compass properties
    maj_txt = compass.radius / 20
    min_txt = maj_txt / 2

    result = []  # list to hold all of the returned objects
    for circle in compass.all_boundary_circles:
        result.append(from_arc2d(circle, z))

    # generate the labels and tick marks for the azimuths
    if custom_angles is None:
        for line in compass.major_azimuth_ticks:
            result.append(from_linesegment2d(line, z))
        for txt, pt in zip(compass.MAJOR_TEXT, compass.major_azimuth_points):
            result.append(text_objects(
                txt, Plane(o=Point3D(pt.x, pt.y, z)), maj_txt, font, 1, 3))
        for line in compass.minor_azimuth_ticks:
            result.append(from_linesegment2d(line, z))
        for txt, pt in zip(compass.MINOR_TEXT, compass.minor_azimuth_points):
            result.append(text_objects(
                txt, Plane(o=Point3D(pt.x, pt.y, z)), min_txt, font, 1, 3))
    else:
        for line in compass.ticks_from_angles(custom_angles):
            result.append(from_linesegment2d(line, z))
        for txt, pt in zip(custom_angles, compass.label_points_from_angles(custom_angles)):
            result.append(text_objects(
                str(txt), Plane(o=Point3D(pt.x, pt.y, z)), maj_txt, font, 1, 3))

    # generate the labels and tick marks for the altitudes
    if projection is not None:
        if projection.title() == 'Orthographic':
            for circle in compass.orthographic_altitude_circles:
                result.append(from_arc2d(circle, z))
            for txt, pt in zip(compass.ALTITUDES, compass.orthographic_altitude_points):
                result.append(text_objects(
                    str(txt), Plane(o=Point3D(pt.x, pt.y, z)), min_txt, font, 1, 0))
        elif projection.title() == 'Stereographic':
            for circle in compass.stereographic_altitude_circles:
                result.append(from_arc2d(circle, z))
            for txt, pt in zip(compass.ALTITUDES, compass.stereographic_altitude_points):
                result.append(text_objects(
                    str(txt), Plane(o=Point3D(pt.x, pt.y, z)), min_txt, font, 1, 0))

    return result
