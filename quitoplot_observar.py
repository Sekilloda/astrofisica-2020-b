# -*- coding: utf-8 -*-
#Programa original: https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html
"""
===================================================================
Determining and plotting the altitude/azimuth of a celestial object
===================================================================

This example demonstrates coordinate transformations and the creation of
visibility curves to assist with observing run planning.

In this example, we make a `~astropy.coordinates.SkyCoord` instance for M33.
The altitude-azimuth coordinates are then found using
`astropy.coordinates.EarthLocation` and `astropy.time.Time` objects.

This example is meant to demonstrate the capabilities of the
`astropy.coordinates` package. For more convenient and/or complex observation
planning, consider the `astroplan <https://astroplan.readthedocs.org/>`_
package.


*By: Erik Tollerud, Kelle Cruz*

*License: BSD*


"""

##############################################################################
# Adaptación para observar desde conocoto
# Importar librerias a ser usadas numpy, matplotlib y astropy.visualization

import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()


##############################################################################
# paquetes para coordenadas y transformación de coordenadas
# 

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

##############################################################################
# `astropy.coordinates.SkyCoord.from_name` usa Simbad para reconocer el nombre del objeto
# simbad: http://simbad.u-strasbg.fr/simbad/
# objetos: M33 (galaxia), Alnitak (estrella central del cinturón de orion, zet Ori en simbad)
#          antares (estrella de la constelación de escorpión alf Sco en simbad)   


m33 = SkyCoord.from_name('M33')
ori=SkyCoord.from_name('zet Ori')
antares=SkyCoord.from_name('alf Sco')
##############################################################################
#`astropy.coordinates.EarthLocation` define la localización de conocoto (lat, long y altitud)
# fecha y tiempo: conocoto, 5 de mayo 2020 a las 20:00
Quito = EarthLocation(lat=0.21*u.deg, lon=-78*u.deg, height=2850*u.m)
utcoffset = -5*u.hour  # Hora local en conocoto (UT-5)
time = Time('2020-5-16 20:00:00') - utcoffset

##############################################################################
#`astropy.coordinates` determina Alt, Az de los objetos M33, Alnitak y Antares 
# el 16 de mayo 2020 a las 20:00

m33altaz = m33.transform_to(AltAz(obstime=time,location=Quito))
orialtaz = ori.transform_to(AltAz(obstime=time,location=Quito))
antaresaltz= antares.transform_to(AltAz(obstime=time,location=Quito))
print("M33's Altitude = {0.alt:.2}".format(m33altaz))
print("ori's Altitude = {0.alt:.2}".format(orialtaz))
print("antares's Altitude = {0.alt:.2}".format(antaresaltz))

##############################################################################
# Masa de aire (air mass) es una medida del espesor de la atmósfera según la posición de
# la estrella. en el zenit ~ 1, en el horizonte 40 
# Determinar alt,az de los objetos 100 en pasos (puntos) desde 20 hasta las 6


midnight = Time('2020-5-16 00:00:00') - utcoffset
delta_midnight = np.linspace(-4, 6, 100)*u.hour
frame_mayo16night = AltAz(obstime=midnight+delta_midnight,
                          location=Quito)
#m33altazs_mayo16night = m33.transform_to(frame_mayo15noche)
orialtazs_mayo16night = ori.transform_to(frame_mayo16night)
antaresaltazs_mayo16night = antares.transform_to(frame_mayo16night)
##############################################################################
# convert alt, az to airmass with `~astropy.coordinates.AltAz.secz` attribute:

#m33airmasss_mayo16night = m33altazs_mayo16night.secz
oriairmasss_mayo16night = orialtazs_mayo16night.secz
antaresairmasss_mayo16night = antaresaltazs_mayo16night.secz
##############################################################################
# Dibujar la masa de aire durante la noche (1 la estrella esta muy alto, 20 esta cerca del horizonte):
# Dijuja solo la masa de aire de antares

plt.plot(delta_midnight, antaresairmasss_mayo16night)
plt.xlim(-4, 6)
plt.ylim(1, 10)
plt.xlabel('Media noche mayo 16 (UT-5)')
plt.ylabel('Airmass [Sec(z)]')
plt.show()

##############################################################################
# `~astropy.coordinates.get_sun` determina la posición del sol en 100 pasos
# el 16 de mayo por la tarde y 17 mayo por la mañana:

from astropy.coordinates import get_sun
delta_midnight = np.linspace(-12, 12, 100)*u.hour
times_mayo16_to_17 = midnight + delta_midnight
frame_mayo16_to_17 = AltAz(obstime=times_mayo16_to_17, location=Quito)
sunaltazs_mayo16_to_17 = get_sun(times_mayo16_to_17).transform_to(frame_mayo16_to_17)


##############################################################################
# `~astropy.coordinates.get_moon`  lo mismo para la luna...
# Se necesita conexión a internet para descargar la información de la posición de la luna ~ 10 MB

from astropy.coordinates import get_moon
moon_mayo16_to_17 = get_moon(times_mayo16_to_17)
moonaltazs_mayo16_to_17 = moon_mayo16_to_17.transform_to(frame_mayo16_to_17)

##############################################################################
# Determinar alt,az en el mismo periodo de tiempo (noche del 16 de mayo):

#m33altazs_mayo16_to_17 = m33.transform_to(frame_mayo16_to_17)
orialtazs_mayo16_to_17 = ori.transform_to(frame_mayo16_to_17)
antaresaltazs_mayo16_to_17 = antares.transform_to(frame_mayo16_to_17)
##############################################################################
# Aquí se define el gráfico
# 

plt.plot(delta_midnight, sunaltazs_mayo16_to_17.alt, color='r', label='sol')
plt.plot(delta_midnight, moonaltazs_mayo16_to_17.alt, color=[0.75]*3, ls='--', label='luna')
plt.scatter(delta_midnight, antaresaltazs_mayo16_to_17.alt,
            c=antaresaltazs_mayo16_to_17.az, label='Antares', lw=0, s=8,
            cmap='viridis')
plt.fill_between(delta_midnight, 0*u.deg, 90*u.deg,
                 sunaltazs_mayo16_to_17.alt < -0*u.deg, color='0.5', zorder=0)
plt.fill_between(delta_midnight, 0*u.deg, 90*u.deg,
                 sunaltazs_mayo16_to_17.alt < -18*u.deg, color='k', zorder=0)
plt.colorbar().set_label('Azimuth [deg]')
plt.legend(loc='upper left')
plt.xlim(-12*u.hour, 12*u.hour)
plt.xticks((np.arange(13)*2-12)*u.hour)
plt.ylim(0*u.deg, 90*u.deg)
plt.xlabel('Mayo 16 media noche (UT-5)')
plt.ylabel('Altitud [deg]')
plt.show()
