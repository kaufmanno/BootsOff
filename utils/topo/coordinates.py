import numpy as np
import folium

def geojson_points_to_feature_group(gjsn, name='Unnamed feature group'):
    """ converts a geojson dictionary into a folium feature group

    :param gjsn: a geojson dictionary
    :type gjsn: dict
    :param name: feature group name
    :param name: str
    :return: a folium feature group
    :rtype: folium.FeatureGroup
    """

    fg = folium.FeatureGroup(name)

    for f in gjsn['features']:
        fg.add_child(folium.Marker(location=flip_coordinates(f['geometry'])['coordinates'],
                                   icon=folium.Icon('icon-circle', icon_color='white')))

    return fg


def flip_coordinates(geom):
    """ flips the coordinates of a geometry object

    :param geom: geojson geometry object
    :type geom: dict
    :return: geom
    :rtype: dict
    """

    if geom['type'] == 'Point':
        z = np.array(geom['coordinates'])
        zf = z.flatten()
        geom['coordinates'] = np.dstack((zf[1::2], zf[::2])).reshape(z.shape).tolist()
    else:
        print('flipping coordinates for %s geometries is not implemented yet...' %geom['type'])
    return geom


def flip_geojson_coordinates(gjsn):
    """ flips geojson geographic coordinates because folium uses the Latitude, Longitude order
    while geojson format is Longitude, Latitude

    Note: checked on points only...

    :param gjsn: a geojson dictionary
    :type gjsn: dict
    :return: status
    :rtype: bool
    """

    status = True
    if isinstance(gjsn, dict):
        # if 'crs' in gjsn.keys():
        #    print(gjsn['crs'])
        # should check if this is WGS84 - need python gdal submodule srs to transform the ofc name into a proj4 string
        # to use pyproj then to check if this is WGS84 or to transform it to WGS84 before flipping coordinates
        if 'type' in gjsn.keys():
            if gjsn['type'] == 'FeatureCollection':
                for f in gjsn['features']:
                    flip_coordinates(f['geometry'])

            else:
                print('type is %s' %gjsn['type'] )
                status = False
        else:
            print('type not in keys...')
            status = False
    else:
        print('Warning!: unable to flip coordinates')
        status = False
    return status


def get_center(obj):
    """ gets the coordinates of the center of the bounding box around a folium object that exposes a get_bounds method

    :param obj; a folium object with the get_bounds method
    :type obj: object
    :return coordinates of the center of the bounding box
    :rtype tuple
    """
    return tuple(np.mean(obj.get_bounds(), axis=0))


if __name__ == '__main__':
    gjsn = {'crs': {'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'},  'type': 'name'},
            'features':
                [{'geometry': {'coordinates': [5.1850604, 50.1414002], 'type': 'Point'},
                  'properties': {'ageofdgpsdata': None, 'cmt': None, 'desc': None, 'dgpsid': None, 'ele': 206.0,
                                 'fix': None, 'geoidheight': None, 'hdop': 5.0, 'speed': 0.1899999976158142,
                                 'src': None, 'sym': None, 'time': '2017/03/26 06:50:41+00', 'track_fid': 0,
                                 'track_seg_id': 0, 'track_seg_point_id': 0, 'type': None, 'vdop': None},
                  'type': 'Feature'},
                 {'geometry': {'coordinates': [5.1850246, 50.1413432], 'type': 'Point'},
                  'properties': {'ageofdgpsdata': None, 'cmt': None, 'desc': None, 'dgpsid': None, 'ele': 208.0,
                                 'fix': None, 'geoidheight': None, 'hdop': 3.0, 'speed': 0.9900000095367432,
                                 'src': None, 'sym': None, 'time': '2017/03/26 06:50:46+00', 'track_fid': 0,
                                 'track_seg_id': 0, 'track_seg_point_id': 1, 'type': None, 'vdop': None},
                  'type': 'Feature'}
                 ],
            'type': 'FeatureCollection'}
    fg = geojson_points_to_feature_group(gjsn)
    print('center:', get_center(fg))
    #flip_coordinates(gjsn)
    #print('flipped center:', get_geojson_center(gjsn))

