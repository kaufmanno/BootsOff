import numpy as np
from os.path import dirname, join
from bootsoff.gravity.constants import G, RT
from bootsoff.gravity.unit_conversions import *
from tidegravity import solve_longman_tide

filename = join(dirname(__file__), 'bullard_table.txt')
bullard_table = np.genfromtxt(filename, delimiter='\t', skip_header=1)


def bullard(h):
    return np.interp(h, bullard_table[:, 0], bullard_table[:, 1])


def convert(value, from_units, to_units):
    error_msg = f'Unknown conversion from {from_units} to {to_units}'
    if from_units == to_units:
        return value
    else:
        try:
            conversion_function = from_units.lower() + '_to_' + to_units.lower()
            return globals()[conversion_function](value)
        except:
            print(error_msg)


def rho(g_above, g_below, h, g0=981, units='mgal'):
    """ Determine the density of a layer from measurements on the top or at the bottom of the layer
    """
    # units: h [m]; g1 & g2 [µgal]; rho [kg/m³]
    g_above = convert(g_above, from_units=units, to_units='si')
    g_below = convert(g_below, from_units=units, to_units='si')
    g0 = convert(g0, from_units=units, to_units='si' )

    rho = ((2*g0/RT)*h+(g_above - g_below))/(4*np.pi*G*h)
    return rho # [kg/m³]


def bouguer_slab(**kwargs):
    # for backwards compatibility
    return g_bs(kwargs)


def g_bs(h, rho, units='mgal'):
    # effect of Bouguer slab
    return convert(2*np.pi*G*rho*h, from_units='si', to_units=units)


def free_air(h, g0=9.81, units='mgal'):
    # effect of free-air
    return convert(-2*g0*h/RT, from_units='si', to_units=units)


def g_etg(phi, units='mgal'):
    """ Ellipsoid Theoretical Gravity
    :param phi: latitude on GRS80 ellipsoid in decimal degrees
    :type: float
    :param units: units for returned value
    :type: str
    :return: Ellipsoid Theoretical Gravity [mgal]
    :rtype float"""
    ge = 978032.67714  # mGal
    k = 0.00193185138639  # values in spreadsheet. They slightly differ from those in the paper ! #TODO: check
    e2 = 0.00669437999013  # values in spreadsheet. They slightly differ from those in the paper ! #TODO: check
    getg = ge * (1 + k * np.sin(deg_to_rad(phi))**2) / np.sqrt(1 - e2 * np.sin(deg_to_rad(phi))**2)
    return convert(getg, from_units='mgal', to_units=units)


def g_atm(h, units='mgal'):
    """ Atmospheric effect
    :param h: height of the gravity station above the GRS80 reference ellipsoid [m]
    :type: float or numpy array
    :param units: units for returned value
    :type: str
    :return: Atmospheric effect [mgal]
    :rtype float"""
    gatm = 0.874 - 9.9 * 10**-5 * h + 3.56 * 10**-9 * h**2
    return convert(gatm, from_units='mgal', to_units=units)


def g_hc(h, phi, units='mgal'):
    """ Height effect to the Theoretical Gravity
    :param h: height of the gravity station above the GRS80 reference ellipsoid [m]
    :param phi: latitude on GRS80 ellispoid in decimal degrees
    :param units: units for returned value
    :type: str"""

    ghc = -(0.308769097 - 0.000439773125 * np.sin(deg_to_rad(phi)) ** 2) * h + 0.0000000721251838 * h ** 2
    return convert(ghc, from_units='mgal', to_units=units)


def g_bsc(h, rho=2670., units='mgal'):
    """ Bouguer Spherical Cap
    :param h: height of the gravity station above the GRS80 reference ellipsoid [m]
    :param rho: density [kg/m³]
    :param units: units for returned value
    :type: str"""

    gbsc = bullard(h) + 2 * np.pi * h * 0.000006673 * rho

    return convert(gbsc, from_units='mgal', to_units=units)


def g_tg(latitude, longitude, height, time, units='mgal'):
    # assumes times given in utc
    _, _, gtg = solve_longman_tide(latitude, longitude, height, time)

    return convert(gtg, from_units='mgal', to_units=units)


def drift_correction(times, base_idx, field='value', method='slinear', from_units='mgal', to_units='mgal'):
    """ Computes the drift correction at given times based on the evolution at a base station
        base_records
    """
    # TODO: Check and improve this
    df_base = df.query('Station_ID == "%s"' % df.loc[base_idx, 'Station_ID']).copy()
    df_base['datetime'] = df_base.index
    df_base['timedelta'] = df_base['datetime'].diff()
    df_base['InstrCorrGrav-Tide'] = df_base['InstrCorrGrav'] - df_base['g_tg']

    df = base_records.sort_index().copy()
    for t in times:
        if t not in base_records.index:
            df.loc[t, field] = np.nan
    df.sort_index(inplace=True)
    df.loc[:, 'dt'] = (df.index - base_records.index[0]).total_seconds()
    df.loc[:, 'idx'] = df.index
    df.set_index('dt', inplace=True)
    df.interpolate(inplace=True, method=method)
    df.rename(columns={'idx': 'time'}, inplace=True)
    df.set_index('time', inplace=True)
    df = df.loc[times,:]
    df.loc[:, 'BaseDriftCorr'] = convert(df[field], from_units=from_units, to_units=to_units)
    return df


def corrections(df, base_idx, rho=2670., units='mgal'):
    # TODO: vérifier si les corrections de dérive doivent être faites avant ces corrections ou après (importance pour la base?)

    e_etg = g_etg(df['Latitude'], units=units)
    df['LatCorr'] = g_etg(df.loc[base_idx, 'Latitude'])-e_etg
    e_atm = g_atm(df['Ellipsoid Height'], units=units)
    df['AtmCorr'] = e_atm.loc[base_idx] - e_atm
    e_hc = g_hc(df['Ellipsoid Height'], df['Latitude'], units=units)
    df['AltCorr'] = e_hc.loc[base_idx] - e_hc
    e_bs = g_bs(df['Ellipsoid Height'], rho, units=units)
    df['BougSlabCorr'] = e_bs.loc[base_idx] - e_bs
    e_bsc = g_bsc(df['Ellipsoid Height'], rho, units=units)
    df['BougSphCapCorr'] = e_bsc.loc[base_idx] - e_bsc
    e_tg = g_tg(df.Latitude, df.Longitude, df['Ellipsoid Height'], df.index.tz_localize(None), units=units)
    df['TideCorr'] = e_tg.loc[base_idx] - e_tg


