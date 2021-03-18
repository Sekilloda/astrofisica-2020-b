import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.coordinates import get_sun, get_moon

plt.style.use(astropy_mpl_style)
plt.rcParams.update({'text.usetex': False, 'font.family':'serif','font.sans-serif':['Helvetica'], 'figure.figsize':(10.6, 7.95), 'figure.dpi':150})
quantity_support()
denebola = SkyCoord.from_name('Beta Leonis')
# `astropy.coordinates.EarthLocation` define la localización de conocoto (lat, long y altitud)
# fecha y tiempo: conocoto, 15 de mayo 2020 a las 22:00
conocoto = EarthLocation(lat=-0.2802732 * u.deg, lon=-78.47801209543195 * u.deg, height=2450 * u.m)
utcoffset = -5 * u.hour  # Hora local en conocoto (UT-5)
time = Time('2021-5-15 22:00:00') - utcoffset
denebola_alt_az = denebola.transform_to(AltAz(obstime=time, location=conocoto))
print(f'Altitud de Denebola {denebola_alt_az.alt:.4f}')
# Masa de aire (air mass) es una medida del espesor de la atmósfera según la posición de
# la estrella. en el zenit ~ 1, en el horizonte 40
# Determinar alt,az de los objetos 10000 en pasos (puntos) desde 22 hasta las 08
midnight = Time('2020-5-15 00:00:00') - utcoffset
delta_midnight_noche = np.linspace(-2, 8, 100) * u.hour
frame_mayo15noche = AltAz(obstime=midnight + delta_midnight_noche,
                          location=conocoto)
denebolaaltazs_mayo15noche = denebola.transform_to(frame_mayo15noche)
denebolaairmass_mayo15noche = denebolaaltazs_mayo15noche.secz
# Dibujar la masa de aire durante la noche (1 la estrella esta muy alto, 40 esta cerca del horizonte):
# Dijuja solo la masa de aire de antares
plt.plot(delta_midnight_noche, denebolaairmass_mayo15noche)
plt.xlim(-2, 8)
plt.ylim(-100, 100)
plt.xlabel('Media noche mayo 15 (UT-5)')
plt.ylabel('Masa de aire [Sec(z)]')
plt.savefig('../images/masadeaire.png')
plt.clf()
delta_midnight = np.linspace(-12, 12, 100) * u.hour
times_mayo15_to_mayo16 = midnight + delta_midnight
frame_mayo15_to_mayo16 = AltAz(obstime=times_mayo15_to_mayo16, location=conocoto)
sunaltazs_mayo15_to_mayo16 = get_sun(times_mayo15_to_mayo16).transform_to(frame_mayo15_to_mayo16)
moonaltazs_mayo15_to_mayo16 = get_moon(times_mayo15_to_mayo16).transform_to(frame_mayo15_to_mayo16)
denebolaaltazs_mayo15_to_mayo16 = denebola.transform_to(frame_mayo15_to_mayo16)
# Aquí se define el gráfico
#
plt.plot(delta_midnight, sunaltazs_mayo15_to_mayo16.alt/u.deg, color='r', label='Sol')
plt.plot(delta_midnight, moonaltazs_mayo15_to_mayo16.alt/u.deg, color=[0.75] * 3, ls='--', label='Luna')
plt.scatter(delta_midnight, denebolaaltazs_mayo15_to_mayo16.alt/u.deg,
            c=denebolaaltazs_mayo15_to_mayo16.az/u.deg, label='Denebola', lw=0, s=8,
            cmap='viridis')
plt.fill_between(delta_midnight, 0, 90,
                 sunaltazs_mayo15_to_mayo16.alt/u.deg < -0, color='0.5', zorder=0)
plt.fill_between(delta_midnight, 0, 90,
                 sunaltazs_mayo15_to_mayo16.alt/u.deg < -18, color='k', zorder=0)
plt.colorbar().set_label('Azimut [grados]')
plt.legend(loc='upper left')
plt.xlim(-12 * u.hour, 12 * u.hour)
plt.xticks((np.arange(13) * 2 - 12) * u.hour)
plt.ylim(0, 90)
plt.xlabel('Mayo 15 media noche en 0 (UT-5)')
plt.ylabel('Altitud [grados]')
plt.title('Altitud y azimut de Denebola')
plt.savefig('../images/estrellacump.png')
