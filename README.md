# Struttura della Galassia

Jupyter notebook utilizzato per l'esperienza "La struttura della Galassia" del *Laboratorio di Modellizazione Dati* A.A. 2025-2026 @UNIMI.

Lavoro di gruppo svolto da S. M. Di Paolo, S. Lonardoni, M. Mirabelli, F. Paris.

## Dati

Dati utilizzati dalla missione GAIA DR3 ottenuti con la sequente query AQDL:
```SQL
SELECT ra, dec, parallax, parallax_error, pmra,
pmra_error, pmdec, pmdec_error,
phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag,
radial_velocity, radial_velocity_error, l, b
FROM gaiadr2.gaia_source
WHERE parallax_error < parallax*0.2 and
radial_velocity_error < 5 and random_index < 100000000
```

## Acknowledgement
This work has made use of data from the European Space Agency (ESA) mission
*Gaia* ([https://www.cosmos.esa.int/gaia](https://www.cosmos.esa.int/gaia)), processed by the *Gaia*
Data Processing and Analysis Consortium (DPAC,
[https://www.cosmos.esa.int/web/gaia/dpac/consortium](https://www.cosmos.esa.int/web/gaia/dpac/consortium)). Funding for the DPAC
has been provided by national institutions, in particular the institutions
participating in the *Gaia* Multilateral Agreement.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.
