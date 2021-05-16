import numpy as np


def si_to_microgal(x):
    # SI [m/s²], gal[10e-2 m/s²], µgal [10e-8 m/s²]
    return x * 1e8


def si_to_mgal(x):
    # SI [m/s²], gal[10e-2 m/s²], mgal [10e-5 m/s²]
    return x * 1e5


def microgal_to_si(x):
    # SI [m/s²], gal[10e-2 m/s²], µgal [10e-8 m/s²]
    return x * 1e-8


def mgal_to_si(x):
    # SI [m/s²], gal[10e-2 m/s²], mgal [10e-5 m/s²]
    return x * 1e-5


def cgs_to_si(x):
    # SI [m/s²], cgs [cm/s²]
    return x * 1e-2


def mgal_to_microgal(x):
    # SI [m/s²], µgal[10e-8 m/s²], mgal [10e-5 m/s²]
    return x * 1e3


def microgal_to_mgal(x):
    # SI [m/s²], µgal[10e-8 m/s²], mgal [10e-5 m/s²]
    return x * 1e-3


def deg_to_rad(phi):
    return phi * np.pi / 180.
