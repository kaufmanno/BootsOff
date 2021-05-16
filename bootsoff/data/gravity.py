import os
from bootsoff.gravity.instruments import import_cg6

filename = os.path.join(os.path.dirname(__file__), 'datasets', 'Data_Profile1')

profile = import_cg6(filename, sep=',',
                     corrections={'TideCorr': 0, 'TiltCorr': 1, 'na': 0, 'TempCorr': 1, 'DriftCorr': 1},
                     keep=['Station_ID', 'InstrCorrGrav', 'StdDev', 'StdErr', 'Latitude', 'Longitude',
                           'Ellipsoid Height', 'InstrHeight', 'RMS Easting', 'RMS Elevation', 'RMS Northing', 'mask',
                           'geometry'])
