from astropy.table import Table
gaia = Table.read("Gaia.vot.gz")

# Posizione(l, b)

l = gaia['l']
b = gaia['b']

# Parallasse

parallax = gaia['parallax']
parallax_err = gaia['parallax_error']

# Velocità Radiale

rv = gaia['radial_velocity']
rv_err = gaia['radial_velocity_error']

# Moto Proprio

pmra = gaia['pmra']
pmdec = gaia['pmdec']

# Considerare solo stelle vicine al piano galattico

import numpy as np

mask = (
    (np.abs(b) < 5) &
    (parallax > 0) &
    (parallax_err / parallax < 0.2) &
    (~np.isnan(rv))
)

data = gaia[mask]

# Distanza

d = 1 / data['parallax']  # in kpc
