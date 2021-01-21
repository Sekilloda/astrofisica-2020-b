import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.coordinates import get_sun, get_moon
plt.style.use(astropy_mpl_style)
quantity_support()
denebola=SkyCoord.from_name('Beta Leonis')
#`astropy.coordinates.EarthLocation` define la localización de conocoto (lat, long y altitud)
# fecha y tiempo: conocoto, 15 de mayo 2020 a las 22:00
conocoto = EarthLocation(lat=-0.2802732 * u.deg, lon=-78.47801209543195 * u.deg, height=2450 * u.m)
utcoffset = -5*u.hour  # Hora local en conocoto (UT-5)
time = Time('2021-5-15 22:00:00') - utcoffset
denebola_alt_az=denebola.transform_to(AltAz(obstime=time, location=conocoto))
print(f'Altitud de Denebola {denebola_alt_az.alt:.4f}')
# Masa de aire (air mass) es una medida del espesor de la atmósfera según la posición de
# la estrella. en el zenit ~ 1, en el horizonte 40
# Determinar alt,az de los objetos 10000 en pasos (puntos) desde 22 hasta las 08
midnight = Time('2020-5-15 00:00:00') - utcoffset
delta_midnight_noche = np.linspace(-2, 8, 100) * u.hour
frame_mayo15noche = AltAz(obstime=midnight + delta_midnight_noche,
                          location=conocoto)
denebolaaltazs_mayo15noche = denebola.transform_to(frame_mayo15noche)
denebolaairmass_mayo15noche=denebolaaltazs_mayo15noche.secz
# Dibujar la masa de aire durante la noche (1 la estrella esta muy alto, 40 esta cerca del horizonte):
# Dijuja solo la masa de aire de antares
plt.plot(delta_midnight_noche, denebolaairmass_mayo15noche)
plt.xlim(-2, 8)
plt.ylim(-100, 100)
plt.xlabel('Media noche mayo 15 (UT-5)')
plt.ylabel('Masa de aire [Sec(z)]')
plt.savefig('masadeaire.png')




