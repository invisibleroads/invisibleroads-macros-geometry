from invisibleroads_macros_geometry import (
    drop_z, flip_xy, transform_geometries)
from shapely.geometry import (
    GeometryCollection,
    LineString,
    Point,
    Polygon)


def test_transform_geometries():
    assert tuple(transform_geometries([
        Point(1, 2),
    ], flip_xy)[0].coords[0]) == (2, 1)

    assert tuple(transform_geometries([
        LineString([(0, 1), (1, 2)]),
    ], flip_xy)[0].coords[0]) == (1, 0)

    assert tuple(transform_geometries([
        Polygon([(0, 1), (1, 2), (2, 3)]),
    ], flip_xy)[0].exterior.coords[0]) == (1, 0)

    assert tuple(transform_geometries([
        GeometryCollection([
            Point(1, 2),
        ]),
    ], flip_xy)[0].geoms[0].coords[0]) == (2, 1)


def test_flip_xy():
    xyz = [1, 2, 3]
    assert flip_xy(xyz) == (2, 1, 3)
    assert xyz == [1, 2, 3]


def test_drop_z():
    xyz = [1, 2, 3]
    assert drop_z(xyz) == (1, 2)
