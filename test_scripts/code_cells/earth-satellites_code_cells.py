%pylab inline
pylab.rcParams['figure.figsize'] = (8.0, 7.0)
pylab.rcParams['font.size'] = 14

#elements = """ISS (ZARYA)             
#1 25544U 98067A   13330.58127943  .00000814  00000-0  21834-4 0  1064
#2 25544  51.6484  23.7537 0001246  74.1647  18.7420 15.50540527859894
#"""

#from skyfield.api import earth
#topos = earth.topos('75 W', '35 N')
#sat = earth.satellite(elements.splitlines())

from itertools import izip, islice
with open('visual.txt', 'r') as f:
    for next_n_lines in izip(*[f] * 3):
        sleep(1)
        print next_n_lines

! List Satellites

from time import sleep
rw = raw_input("Name : ")
print rw
with open('visual.txt', 'r') as f:
    while True:
            name = f.readline()
            one = f.readline()
            two = f.readline()
            sleep(1)
            if name == rw:
                print "HERE :",name, one, two
                print name, one, two    
            if not one: break  # EOF
        
 

%%writefile SatInfo.py
from itertools import izip, islice
from time import sleep
def satinfo():
    search_string = raw_input("Load : ")
    with open('visual.txt', 'r') as infile, open('visual.tmp', 'w') as outfile:
        for line in infile:
            if search_string in line:
                outfile.writelines([line, next(infile), next(infile)])

    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                return name, one, two    
                         
def prntlist():            
    from time import sleep
    with open('visual.txt', 'r') as f:
        while True:
            next_n_lines = list(islice(f, 3))
            if not next_n_lines:
                break
            sleep(.5)
            print next_n_lines[0],
        
def reuse():
    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                #print name, one, two    
                f.close()
                return name, one, two  
            
            

!rm SatInfo.pyc

import SatInfo
print SatInfo.satinfo()

import SatInfo
SatInfo.prntlist()

import SatInfo
a,b,c = SatInfo.reuse()
print a,b,c

from time import sleep
with open('ALL_TLE.TXT', 'r') as f:
    while True:
        next_n_lines = list(islice(f, 3))
        if not next_n_lines:
            break

        sleep(1)
        print next_n_lines[0],

from time import sleep
with open('visual.tmp', 'r') as f:
    while True:
            name = f.readline()
            one = f.readline()
            two = f.readline()
            sleep(1)
            print name, one, two    
            if not one: break  # EOF
        
 

from time import sleep
with open('ALL_TLE.TXT', 'r') as f:
    lines = f.readlines()
    for line in lines:
        sleep(1)
        print line



from time import sleep
with open('visual.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        sleep(1)
        print line

!ls *.txt

# based on 'grouper()' example from the python 2 itertools documentation
from itertools import izip
def partition(lines, n):
    iters = [iter(lines)] * n
    return izip(*iters)

import skyfield
help(skyfield)

import skyfield.api
help(skyfield.api)

from skyfield.api import JulianDate, earth, utc, EarthSatellite
help(EarthSatellite)

import numpy as np
import matplotlib.pyplot as plt

from skyfield.api import load

planets = load('de421.bsp')

earth   = planets['earth']
mars    = planets['mars']

year_zero = 2010
days = np.linspace(1, 3650, 10000)
years = year_zero + days / 365.2564
ts = load.timescale()
t = ts.utc(year_zero, 1, days)

# thanks to @barrycarter's comment, do it the right way!
eclat, eclon, ecd = earth.at(t).observe(mars).ecliptic_latlon()

eclondgs      = (180./np.pi) * eclon.radians
eclondel      = eclondgs[1:] - eclondgs[:-1]

eclondel[eclondel < -300] += 360. # this is a fudge for now
eclondel[eclondel > +300] -= 360. # this is a fudge for now

prograde   = eclondel > 0.

eclon_prograde   = eclondgs.copy()[:-1]
eclon_retrograde = eclondgs.copy()[:-1]

eclon_prograde[-prograde]  = np.nan
eclon_retrograde[prograde] = np.nan

plt.figure()
plt.plot(years[:-1], eclon_prograde,   '-g', linewidth=1)
plt.plot(years[:-1], eclon_retrograde, '-r', linewidth=3)
plt.ylim(0, 360)
plt.title('Mars Ecliptic longitude (degrees) AD 2010.0 to 2020.0',
          fontsize=16)
plt.show()

from skyfield.api import JulianDate, earth, utc, EarthSatellite

tle = """
GOCE                    
1 34602U 09013A   13314.96046236  .14220718  20669-5  50412-4 0   930
2 34602 096.5717 344.5256 0009826 296.2811 064.0942 16.58673376272979
"""
print x,y =tle[0:]

from skyfield.api import EarthSatellite
import SatInfo
a,b,c = SatInfo.reuse()

sat = EarthSatellite(b, c, a)
print(sat.epoch.utc_jpl())

from skyfield.api import JulianDate, earth, utc
from skyfield.api import EarthSatellite

a = '1 34602U 09013A   13314.96046236  .14220718  20669-5  50412-4 0   930'
b = '2 34602 096.5717 344.5256 0009826 296.2811 064.0942 16.58673376272979'
c = 'GOCE' 

sat = EarthSatellite(a,b,c)
print(sat.epoch.utc_jpl())

from skyfield.api import JulianDate, earth, utc
from skyfield.api import EarthSatellite
from skyfield.api import load
help(sat)

from skyfield.api import load
ts = load.timescale()
reentry = ts.utc(1980, 4, 20)       # the new way
t = ts.tt(jd=2444349.500592)  # jd is also supported for tai, tt, tdb



x= 2,6,4,5,7,8,9,5,45
y= 12,26,4,15,7,18,9,15,45

plot(x, y)

#reentry = JulianDate(utc=(2013, 11, 11, 0, 16))

for j, label in [(sat.epoch, 'Epoch of TLE data'),
                 (reentry, 'Actual moment of re-entry')]:
    px = j.toordinal()
    py = sat.gcrs(j).distance().km - earth.radius.km
    plot(px, py, 'ro')
    text(px, py + 10, label)

xaxis = axes().xaxis
xaxis.grid(True)
xaxis.set_major_locator(HourLocator([0]))
xaxis.set_minor_locator(HourLocator([0, 12]))
xaxis.set_major_formatter(DateFormatter('\n%a %d'))
xaxis.set_minor_formatter(DateFormatter('%Hh'))

yaxis = axes().yaxis
yaxis.grid(True)

ISS_TLE = """1 25544U 98067A   16341.96974289  .00003303  00000-0  57769-4 0  9996
2 25544  51.6456 276.4739 0005937 300.1004 104.8148 15.53811586 31866"""

import numpy as np
import matplotlib.pyplot as plt
from skyfield.api import load, Topos
degs     = 180./np.pi

r_earth  = 6371.  # for approx. ground track, just use spherical Earth

data     = load('de421.bsp')
Earth    = data['earth']
ZeroZero = Earth+Topos(0.0, 0.0)
ISS      = Earth.satellite(ISS_TLE)

ts       = load.timescale()
minutes  = np.arange(0, 12*60, 1)
time     = ts.utc(2016, 12, 7, 12, minutes)

Epos     = Earth.at(time).position.km
ZZpos    = ZeroZero.at(time).position.km - Epos   ## Position of (0.0N, 0.0E) to get rotation
ISSpos   = ISS._position_and_velocity_TEME_km(time)[0] ## semi-private method, unellegant use

theta_ZZ = np.arctan2(ZZpos[1], ZZpos[0])   # calculate Earth's rotaion

sth, cth         = np.sin(-theta_ZZ), np.cos(-theta_ZZ) # unwind
xISS, yISS, zISS = ISSpos
xISSnew, yISSnew = xISS*cth - yISS*sth, xISS*sth + yISS*cth # rotate ISS data to match Earth
ISSnew           = np.vstack((xISSnew, yISSnew, zISS))

x, y, z = ISSnew
r       = np.sqrt((ISSpos**2).sum(axis=0))
rxy     = np.sqrt(x**2 + y**2)
ISSlat, ISSlon   = np.arctan2(z, rxy), np.arctan2(y, x)

plt.figure()
plt.plot(degs*ISSlon, degs*ISSlat, 'ok')
plt.show()


http://rhodesmill.org/skyfield/toc.html

from skyfield.api import load

planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']

ts = load.timescale()
t = ts.now()
astrometric = earth.at(t).observe(mars)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)


from skyfield.api import Topos

boston = earth + Topos('42.3583 N', '71.0636 W')
astrometric = boston.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)

from astropy import units as u
xyz = astrometric.position.to(u.au)
altitude = alt.to(u.deg)

print(xyz)
print('{0:0.03f}'.format(altitude))


from skyfield.api import load
ts = load.timescale()
planets = load('de405.bsp')


from skyfield import api
ts = api.load_timescale()

from skyfield.api import Topos, load

ts = load.timescale()
t = ts.now()

planets = load('de421.bsp')
earth = planets['earth']
mars = planets['mars']

# From the center of the Solar System (Barycentric)

barycentric = mars.at(t)

# From the center of the Earth (Geocentric)

astrometric = earth.at(t).observe(mars)
apparent = earth.at(t).observe(mars).apparent()

# From a place on Earth (Topocentric)

boston = earth + Topos('42.3583 N', '71.0603 W')
astrometric = boston.at(t).observe(mars)
apparent = boston.at(t).observe(mars).apparent()
print apparent

# BCRS positions of Earth and Venus

from skyfield.api import load

planets = load('de421.bsp')
earth = planets['earth']
mars = planets['mars']

t = ts.utc(1980, 1, 1)
print(earth.at(t).position.au)
print(mars.at(t).position.au)

# Observing Mars from the Earth's position

astrometric = earth.at(ts.utc(1980, 1, 1)).observe(mars)
print(astrometric.position.au)

# Astrometric RA and declination

ra, dec, distance = astrometric.radec()
print(ra.hstr())
print(dec.dstr())
print(distance)

import Here
print Here.here()[0],"N"
print Here.here()[1],"W"

from skyfield.api import Star, Topos, load
from datetime import datetime
import Here
laT = (Here.here()[0]+" N")
loN = (Here.here()[1]+" W")

t = ts.utc(1980, 1, 1)
#Manila = earth + Topos(laT, loN)
boston = earth + Topos('42.3583 N', '71.0603 W')
barnard = Star(ra_hours=(17, 57, 48.49803),
               dec_degrees=(4, 41, 36.2072))

# From the center of the Earth (Geocentric)

astrometric = earth.at(t).observe(barnard)
apparent = earth.at(t).observe(barnard).apparent()

# From a place on Earth (Topocentric)

astrometric = boston.at(t).observe(barnard)
apparent = boston.at(t).observe(barnard).apparent()


from skyfield.api import Topos, load
import Here
laT = (Here.here()[0]+" N")
loN = (Here.here()[1]+" W")

ts = load.timescale()
t = ts.now()

planets = load('de421.bsp')
earth = planets['earth']
mars = planets['mars']

# From the center of the Solar System (Barycentric)

barycentric = mars.at(t)

# From the center of the Earth (Geocentric)

astrometric = earth.at(t).observe(mars)
apparent = earth.at(t).observe(mars).apparent()

# From a place on Earth (Topocentric)

#boston = earth + Topos('42.3583 N', '71.0603 W')
manila = earth + Topos(laT, loN)
astrometric = manila.at(t).observe(mars)
apparent = manila.at(t).observe(mars).apparent()


# Apparent GCRS ("J2000.0") coordinates

apparent = astrometric.apparent()
ra, dec, distance = apparent.radec()

print(ra.hstr())
print(dec.dstr())
print(distance)


from skyfield.api import Star, Topos, load
from datetime import datetime
import Here
laT = (Here.here()[0]+" N")
loN = (Here.here()[1]+" W")
print laT,loN

alt, az, distance = apparent.altaz()

from skyfield.api import Topos, load
import Here
laT = (Here.here()[0]+" N")
loN = (Here.here()[1]+" W")



# Altitude and azimuth in the sky of a
# specific geographic location
manila = earth + Topos(laT, loN)
#boston = earth + Topos('42.3583 N', '71.0603 W')
astro = manila.at(ts.utc(2017, 10, 17)).observe(mars)
app = astro.apparent()

alt, az, distance = app.altaz()
print(alt.dstr())
print(az.dstr())
print(distance)

http://panahon.observatory.ph/

alt, az, distance = app.altaz(temperature_C=32.0,
                              pressure_mbar=1005.6)
print(alt.dstr())

alt, az, distance = app.altaz('standard')
print(alt.dstr())

from skyfield.api import Topos, load

stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle(stations_url)
satellite = satellites['ISS (ZARYA)']
print(satellite)

print(satellite.epoch)
print(satellite.epoch.utc_jpl())

ts = load.timescale()
t = ts.utc(2017, 10, 17, 12, 18, 7)

days = t - satellite.epoch
print('{:.3f} days away from epoch'.format(days))

if abs(days) > 14:
    satellites = load.tle(stations_url, reload=True)
    satellite = satellites['ISS (ZARYA)']

geocentric = satellite.at(t)
print(geocentric.position.km)


bluffton = Topos('40.8939 N', '83.8917 W')
difference = satellite - bluffton
print(difference)

topocentric = difference.at(t)
print(topocentric.position.km)

alt, az, distance = topocentric.altaz()

if alt.degrees > 0:
    print('The ISS is above the horizon')

print(alt)
print(az)
print(distance.km)

ra, dec, distance = topocentric.radec()  # ICRF ("J2000")
print(ra)
print(dec)

ra, dec, distance = topocentric.radec(epoch='date')
print(ra)
print(dec)

# OVERLY EXPENSIVE APPROACH - Compute both the satellite
# and observer positions relative to the Solar System
# barycenter ("ssb"), then call observe() to compensate
# for light-travel time.

de421 = load('de421.bsp')
earth = de421['earth']
ssb_bluffton = earth + bluffton
ssb_satellite = earth + satellite
topocentric2 = ssb_bluffton.at(t).observe(ssb_satellite).apparent()

# After all that work, how big is the difference, really?
difference_km = (topocentric2 - topocentric).distance().km
print('Difference between the two positions:')
print('{0:.3f} km'.format(difference_km))

difference_angle = topocentric2.separation_from(topocentric)
print('Angle between the two positions in the sky:')
print('{}'.format(difference_angle))

from skyfield.api import EarthSatellite
import SatInfo
a,b,c = SatInfo.reuse()

sat = EarthSatellite(b,c,a)

print sat

#%%writefile TLE.py
#!/usr/bin/python
# -*- coding: ascii -*-
import numpy as np
import pylab as plt
import ephem
import datetime
from skyfield.api import EarthSatellite
import SatInfo
a,b,c = SatInfo.reuse()
# Setup lat long of telescope
oxford = ephem.Observer()
oxford.lat = np.deg2rad(51.75)
oxford.long = np.deg2rad(-1.259)
oxford.date = datetime.datetime.now()
#Satillite info from SatInfo Module
biif1 = ephem.readtle(a,b,c)
# Make datetimes
midnight = datetime.datetime.replace(datetime.datetime.now(), hour=0)
dt  = [midnight + datetime.timedelta(minutes=20*x) for x in range(0, 24*3)]
# Compute satellite locations at each datetime
sat_alt, sat_az = [], []
for date in dt:
    oxford.date = date
    biif1.compute(oxford)
    sat_alt.append(np.rad2deg(biif1.alt))
    sat_az.append(np.rad2deg(biif1.az))
# Satellite Tracks
plt.subplot(211)
plt.plot(dt, sat_alt)
plt.ylabel("Altitude (deg)")
plt.xticks(rotation=25)
plt.subplot(212)
plt.plot(dt, sat_az)
plt.ylabel("Azimuth (deg)")
plt.xticks(rotation=25)
plt.show()
# Satellite Polar Coordinates
plt.polar(np.deg2rad(sat_az), 90-np.array(sat_alt))
plt.ylim(0,90)
plt.show()
def loadTLE(filename):
    """ Loads a TLE file and creates a list of satellites."""
    f = open(filename)
    satlist = []
    l1 = f.readline()
    while l1:
        l2 = f.readline()
        l3 = f.readline()
        sat = ephem.readtle(l1,l2,l3)
        satlist.append(sat)
        print sat.name
        l1 = f.readline()

    f.close()
    print "%i satellites loaded into list"%len(satlist)
    return satlist
loadTLE('ALL_TLE.TXT')

from skyfield.api import EarthSatellite
import SatInfo
a,b,c = SatInfo.reuse()

print a, b, c

%%writefile SatInfo.py
from itertools import izip, islice
from time import sleep
def satinfo():
    search_string = raw_input("Load : ")
    with open('visual.txt', 'r') as infile, open('visual.tmp', 'w') as outfile:
        for line in infile:
            if search_string in line:
                outfile.writelines([line, next(infile), next(infile)])

    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                return name, one, two    
                         
def prntlist():            
    from time import sleep
    with open('visual.txt', 'r') as f:
        while True:
            next_n_lines = list(islice(f, 3))
            if not next_n_lines:
                break
            sleep(.5)
            print next_n_lines[0],
        
def reuse():
    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                #print name, one, two    
                f.close()
                return name, one, two  
            
            

import SatInfo
a,b,c = SatInfo.reuse()

import SatInfo
SatInfo.prntlist()

import SatInfo
a,b,c = SatInfo.reuse()

from skyfield.api import EarthSatellite
import SatInfo
a,b,c = SatInfo.reuse()

sat = EarthSatellite(b, c, a)
print(sat.epoch.utc_jpl())

from skyfield.api import EarthSatellite
import SatInfo
a,b,c = SatInfo.reuse()
#print a,b,c
#text = """
#GOCE
#1 34602U 09013A   13314.96046236  .14220718  20669-5  50412-4 0   930
#2 34602 096.5717 344.5256 0009826 296.2811 064.0942 16.58673376272979
#"""
#lines = text.strip().splitlines()
sat = EarthSatellite(b, c, a)
#sat = EarthSatellite(lines[1], lines[2], lines[0])
print(sat.epoch.utc_jpl())

from skyfield.api import EarthSatellite
text = """
GOCE
1 34602U 09013A   13314.96046236  .14220718  20669-5  50412-4 0   930
2 34602 096.5717 344.5256 0009826 296.2811 064.0942 16.58673376272979
"""
lines = text.strip().splitlines()

sat = EarthSatellite(lines[1], lines[2], lines[0])
print(sat.epoch.utc_jpl())

geocentric = sat.at(ts.utc(2013, 11, 9))
print('Before:')
print(geocentric.position.km)
print(geocentric.message)

geocentric = sat.at(ts.utc(2013, 11, 13))
print('\nAfter:')
print(geocentric.position.km)
print(geocentric.message)

from pprint import pprint

geocentric = sat.at(ts.utc(2013, 11, [9, 10, 11, 12, 13]))
pprint(geocentric.message)

"""
XKCD plot generator
-------------------
Author: Jake Vanderplas

This is a script that will take any matplotlib line diagram, and convert it
to an XKCD-style plot.  It will work for plots with line & text elements,
including axes labels and titles (but not axes tick labels).

The idea for this comes from work by Damon McDougall
  http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg25499.html
"""
import numpy as np
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm


# We need a special font for the code below.  It can be downloaded this way:
import os
import urllib2
if not os.path.exists('Humor-Sans.ttf'):
    fhandle = urllib2.urlopen('http://antiyawn.com/uploads/Humor-Sans-1.0.ttf')
    open('Humor-Sans.ttf', 'wb').write(fhandle.read())

    
def xkcd_line(x, y, xlim=None, ylim=None,
              mag=1.0, f1=30, f2=0.05, f3=15):
    """
    Mimic a hand-drawn line from (x, y) data

    Parameters
    ----------
    x, y : array_like
        arrays to be modified
    xlim, ylim : data range
        the assumed plot range for the modification.  If not specified,
        they will be guessed from the  data
    mag : float
        magnitude of distortions
    f1, f2, f3 : int, float, int
        filtering parameters.  f1 gives the size of the window, f2 gives
        the high-frequency cutoff, f3 gives the size of the filter
    
    Returns
    -------
    x, y : ndarrays
        The modified lines
    """
    x = np.asarray(x)
    y = np.asarray(y)
    
    # get limits for rescaling
    if xlim is None:
        xlim = (x.min(), x.max())
    if ylim is None:
        ylim = (y.min(), y.max())

    if xlim[1] == xlim[0]:
        xlim = ylim
        
    if ylim[1] == ylim[0]:
        ylim = xlim

    # scale the data
    x_scaled = (x - xlim[0]) * 1. / (xlim[1] - xlim[0])
    y_scaled = (y - ylim[0]) * 1. / (ylim[1] - ylim[0])

    # compute the total distance along the path
    dx = x_scaled[1:] - x_scaled[:-1]
    dy = y_scaled[1:] - y_scaled[:-1]
    dist_tot = np.sum(np.sqrt(dx * dx + dy * dy))

    # number of interpolated points is proportional to the distance
    Nu = int(200 * dist_tot)
    u = np.arange(-1, Nu + 1) * 1. / (Nu - 1)

    # interpolate curve at sampled points
    k = min(3, len(x) - 1)
    res = interpolate.splprep([x_scaled, y_scaled], s=0, k=k)
    x_int, y_int = interpolate.splev(u, res[0]) 

    # we'll perturb perpendicular to the drawn line
    dx = x_int[2:] - x_int[:-2]
    dy = y_int[2:] - y_int[:-2]
    dist = np.sqrt(dx * dx + dy * dy)

    # create a filtered perturbation
    coeffs = mag * np.random.normal(0, 0.01, len(x_int) - 2)
    b = signal.firwin(f1, f2 * dist_tot, window=('kaiser', f3))
    response = signal.lfilter(b, 1, coeffs)

    x_int[1:-1] += response * dy / dist
    y_int[1:-1] += response * dx / dist

    # un-scale data
    x_int = x_int[1:-1] * (xlim[1] - xlim[0]) + xlim[0]
    y_int = y_int[1:-1] * (ylim[1] - ylim[0]) + ylim[0]
    
    return x_int, y_int


def XKCDify(ax, mag=1.0,
            f1=50, f2=0.01, f3=15,
            bgcolor='w',
            xaxis_loc=None,
            yaxis_loc=None,
            xaxis_arrow='+',
            yaxis_arrow='+',
            ax_extend=0.1,
            expand_axes=False):
    """Make axis look hand-drawn

    This adjusts all lines, text, legends, and axes in the figure to look
    like xkcd plots.  Other plot elements are not modified.
    
    Parameters
    ----------
    ax : Axes instance
        the axes to be modified.
    mag : float
        the magnitude of the distortion
    f1, f2, f3 : int, float, int
        filtering parameters.  f1 gives the size of the window, f2 gives
        the high-frequency cutoff, f3 gives the size of the filter
    xaxis_loc, yaxis_log : float
        The locations to draw the x and y axes.  If not specified, they
        will be drawn from the bottom left of the plot
    xaxis_arrow, yaxis_arrow : str
        where to draw arrows on the x/y axes.  Options are '+', '-', '+-', or ''
    ax_extend : float
        How far (fractionally) to extend the drawn axes beyond the original
        axes limits
    expand_axes : bool
        if True, then expand axes to fill the figure (useful if there is only
        a single axes in the figure)
    """
    # Get axes aspect
    ext = ax.get_window_extent().extents
    aspect = (ext[3] - ext[1]) / (ext[2] - ext[0])

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xspan = xlim[1] - xlim[0]
    yspan = ylim[1] - xlim[0]

    xax_lim = (xlim[0] - ax_extend * xspan,
               xlim[1] + ax_extend * xspan)
    yax_lim = (ylim[0] - ax_extend * yspan,
               ylim[1] + ax_extend * yspan)

    if xaxis_loc is None:
        xaxis_loc = ylim[0]

    if yaxis_loc is None:
        yaxis_loc = xlim[0]

    # Draw axes
    xaxis = pl.Line2D([xax_lim[0], xax_lim[1]], [xaxis_loc, xaxis_loc],
                      linestyle='-', color='k')
    yaxis = pl.Line2D([yaxis_loc, yaxis_loc], [yax_lim[0], yax_lim[1]],
                      linestyle='-', color='k')

    # Label axes3, 0.5, 'hello', fontsize=14)
    ax.text(xax_lim[1], xaxis_loc - 0.02 * yspan, ax.get_xlabel(),
            fontsize=14, ha='right', va='top', rotation=12)
    ax.text(yaxis_loc - 0.02 * xspan, yax_lim[1], ax.get_ylabel(),
            fontsize=14, ha='right', va='top', rotation=78)
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Add title
    ax.text(0.5 * (xax_lim[1] + xax_lim[0]), yax_lim[1],
            ax.get_title(),
            ha='center', va='bottom', fontsize=16)
    ax.set_title('')

    Nlines = len(ax.lines)
    lines = [xaxis, yaxis] + [ax.lines.pop(0) for i in range(Nlines)]

    for line in lines:
        x, y = line.get_data()

        x_int, y_int = xkcd_line(x, y, xlim, ylim,
                                 mag, f1, f2, f3)

        # create foreground and background line
        lw = line.get_linewidth()
        line.set_linewidth(2 * lw)
        line.set_data(x_int, y_int)

        # don't add background line for axes
        if (line is not xaxis) and (line is not yaxis):
            line_bg = pl.Line2D(x_int, y_int, color=bgcolor,
                                linewidth=8 * lw)

            ax.add_line(line_bg)
        ax.add_line(line)

    # Draw arrow-heads at the end of axes lines
    arr1 = 0.03 * np.array([-1, 0, -1])
    arr2 = 0.02 * np.array([-1, 0, 1])

    arr1[::2] += np.random.normal(0, 0.005, 2)
    arr2[::2] += np.random.normal(0, 0.005, 2)

    x, y = xaxis.get_data()
    if '+' in str(xaxis_arrow):
        ax.plot(x[-1] + arr1 * xspan * aspect,
                y[-1] + arr2 * yspan,
                color='k', lw=2)
    if '-' in str(xaxis_arrow):
        ax.plot(x[0] - arr1 * xspan * aspect,
                y[0] - arr2 * yspan,
                color='k', lw=2)

    x, y = yaxis.get_data()
    if '+' in str(yaxis_arrow):
        ax.plot(x[-1] + arr2 * xspan * aspect,
                y[-1] + arr1 * yspan,
                color='k', lw=2)
    if '-' in str(yaxis_arrow):
        ax.plot(x[0] - arr2 * xspan * aspect,
                y[0] - arr1 * yspan,
                color='k', lw=2)

    # Change all the fonts to humor-sans.
    prop = fm.FontProperties(fname='Humor-Sans.ttf', size=16)
    for text in ax.texts:
        text.set_fontproperties(prop)
    
    # modify legend
    leg = ax.get_legend()
    if leg is not None:
        leg.set_frame_on(False)
        
        for child in leg.get_children():
            if isinstance(child, pl.Line2D):
                x, y = child.get_data()
                child.set_data(xkcd_line(x, y, mag=10, f1=100, f2=0.001))
                child.set_linewidth(2 * child.get_linewidth())
            if isinstance(child, pl.Text):
                child.set_fontproperties(prop)
    
    # Set the axis limits
    ax.set_xlim(xax_lim[0] - 0.1 * xspan,
                xax_lim[1] + 0.1 * xspan)
    ax.set_ylim(yax_lim[0] - 0.1 * yspan,
                yax_lim[1] + 0.1 * yspan)

    # adjust the axes
    ax.set_xticks([])
    ax.set_yticks([])      

    if expand_axes:
        ax.figure.set_facecolor(bgcolor)
        ax.set_axis_off()
        ax.set_position([0, 0, 1, 1])
    
    return ax


%pylab inline

np.random.seed(0)

ax = pylab.axes()

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x) * np.exp(-0.1 * (x - 5) ** 2), 'b', lw=1, label='damped sine')
ax.plot(x, -np.cos(x) * np.exp(-0.1 * (x - 5) ** 2), 'r', lw=1, label='damped cosine')

ax.set_title('check it out!')
ax.set_xlabel('x label')
ax.set_ylabel('y label')

ax.legend(loc='lower right')

ax.set_xlim(0, 10)
ax.set_ylim(-1.0, 1.0)

#XKCDify the axes -- this operates in-place
XKCDify(ax, xaxis_loc=0.0, yaxis_loc=1.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=True)

# Some helper functions
def norm(x, x0, sigma):
    return np.exp(-0.5 * (x - x0) ** 2 / sigma ** 2)

def sigmoid(x, x0, alpha):
    return 1. / (1. + np.exp(- (x - x0) / alpha))
    
# define the curves
x = np.linspace(0, 1, 100)
y1 = np.sqrt(norm(x, 0.7, 0.05)) + 0.2 * (1.5 - sigmoid(x, 0.8, 0.05))

y2 = 0.2 * norm(x, 0.5, 0.2) + np.sqrt(norm(x, 0.6, 0.05)) + 0.1 * (1 - sigmoid(x, 0.75, 0.05))

y3 = 0.05 + 1.4 * norm(x, 0.85, 0.08)
y3[x > 0.85] = 0.05 + 1.4 * norm(x[x > 0.85], 0.85, 0.3)

# draw the curves
ax = pl.axes()
ax.plot(x, y1, c='gray')
ax.plot(x, y2, c='blue')
ax.plot(x, y3, c='red')

ax.text(0.3, -0.1, "Yard")
ax.text(0.5, -0.1, "Steps")
ax.text(0.7, -0.1, "Door")
ax.text(0.9, -0.1, "Inside")

ax.text(0.05, 1.1, "fear that\nthere's\nsomething\nbehind me")
ax.plot([0.15, 0.2], [1.0, 0.2], '-k', lw=0.5)

ax.text(0.25, 0.8, "forward\nspeed")
ax.plot([0.32, 0.35], [0.75, 0.35], '-k', lw=0.5)

ax.text(0.9, 0.4, "embarrassment")
ax.plot([1.0, 0.8], [0.55, 1.05], '-k', lw=0.5)

ax.set_title("Walking back to my\nfront door at night:")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1.5)

# modify all the axes elements in-place
XKCDify(ax, expand_axes=True)


def alt_lonlat(lon, lat, t):

    topo = earth.topos(lat, lon)

    alt, az, dist = topo.at(trise).observe(sun).apparent().altaz() ## apparent() args for atmospheric refraction

    return alt.degrees


from skyfield.api import load
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

data  = load('de421.bsp')
ts    = load.timescale()

# your example:  '2014-08-27', sunset = '10:00 PM', sunrise = '7:30 AM'

trise  = ts.utc(2014, 8, 27,  7, 30, 0)
tset   = ts.utc(2014, 8, 27, 22,  0, 0)

earth = data['earth']
sun   = data['sun']

zerozero = earth.topos(0.0, 0.0)   # gotta start looking somewhere!

alt, az, dist = zerozero.at(trise).observe(sun).apparent().altaz() ## apparent() args for atmospheric refraction

print "at trise, JD = ", trise.tt
print "at (0N, 0E) Sun's altitude: ", alt.degrees, "azimuth: ", az.degrees
print "at (0N, 0E) Sun's distance (km): ", dist.km

# Find points on equator where sun is on horizon (rise or set) at t=trise

limits   = ((0, 180.), (180, 360.))
lonzeros = []

for a, b in limits:

    answer, info = spo.brentq(alt_lonlat, a, b,
                              args=(0.0, trise),
                              full_output = True )

    if info.converged:
        lonzeros.append(answer)
        print "limits ", a, b, " converged! Found longitude (deg): ", answer
    else:
        print "limits ", a, b, "whaaaa?"
        lonzeros.append(None)

# make some curves

lats = np.linspace(-60, 60, 13)

longis = []
for lon0 in lonzeros:
    lons = []
    for lat in lats:

        answer, info = spo.brentq(alt_lonlat, lon0-90, lon0+90,
                                  args=(lat, trise),
                                  full_output = True )
        if info.converged:
            lons.append(answer)
        else:
            lons.append(None)

        lons = [(lon+180)%360.-180 for lon in lons]  # wraparound at +/- 180

    longis.append(lons)

plt.figure()

for lons in longis:
    plt.plot(lons, lats)

for lons in longis:
    plt.plot(lons, lats, 'ok')

plt.xlim(-180, 180)
plt.ylim(-90, 90)

plt.title("at trise, JD = " + str(trise.tt))

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from   skyfield.api import load, JulianDate
import time

ephem = 'de421.bsp'
ephem = 'de405.bsp'

de = load(ephem)  

earth            = de['earth']
moon             = de['moon']
earth_barycenter = de['earth barycenter']
mercury          = de['mercury']
jupiter          = de['jupiter barycenter']
pluto            = de['pluto barycenter']

things = [ earth,   moon,   earth_barycenter,   mercury,   jupiter,   pluto ]
names  = ['earth', 'moon', 'earth barycenter', 'mercury', 'jupiter', 'pluto']

ntimes = [i*10**n for n in range(5) for i in [1, 2, 5]]

years  = [np.zeros(1)] + [np.linspace(0, 100, n) for n in ntimes[1:]] # 100 years

microsecs = []
for y in years:

    from skyfield.api import load
    ts = load.timescale()
    t = ts.utc(1980, 4, 20)       # the new way

    jd = ts.tt(jd=2444349.500592)  # jd is also supported for tai, tt, tdb
    
    # Depreciated
    #jd = JulianDate(utc=(1900 + y, 1, 1))
    mics = []
    for thing in things:

        tstart = time.clock()
        answer = thing.at(jd).position.km
        mics.append(1E+06 * (time.clock() - tstart))

    microsecs.append(mics)

microsecs = np.array(microsecs).T

many = [len(y) for y in years]


fig = plt.figure(figsize=(10, 8))
ax  = plt.subplot(111, xlabel='length of JD object',
                       ylabel='microseconds',
                       title='time for thing.at(jd).position.km with ' + ephem )

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(item.get_fontsize() + 4) # http://stackoverflow.com/a/14971193/3904031

for name, mics in zip(names, microsecs):
    ax.plot(many, mics, lw=2, label=name)
plt.legend(loc='upper left', shadow=False, fontsize='x-large')
plt.xscale('log')
plt.yscale('log')
plt.savefig("skyfield speed test " + ephem.split('.')[0])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from jplephem.spk import SPK
import time

ephem = 'de421.bsp'
ephem = 'de405.bsp'

kernel = SPK.open(ephem)

jd_1900_01_01 = 2415020.5004882407

ntimes = [i*10**n for n in range(5) for i in [1, 2, 5]]

years  = [np.zeros(1)] + [np.linspace(0, 100, n) for n in ntimes[1:]] # 100 years

barytup  = (0, 3)
earthtup = (3, 399)
# moontup  = (3, 301)

microsecs = []
for y in years:
    mics = []
    #for thing in things:

    jd = jd_1900_01_01 + y * 365.25 # roughly, it doesn't matter here

    tstart = time.clock()
    answer = kernel[earthtup].compute(jd) + kernel[barytup].compute(jd)
    mics.append(1E+06 * (time.clock() - tstart))

    microsecs.append(mics)

microsecs = np.array(microsecs)

many = [len(y) for y in years]

fig = plt.figure()
ax  = plt.subplot(111, xlabel='length of JD object',
                       ylabel='microseconds',
                       title='time for jplephem [0,3] and [3,399] with ' + ephem )

#   from here: http://stackoverflow.com/a/14971193/3904031
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(item.get_fontsize() + 4)

#for name, mics in zip(names, microsecs):
ax.plot(many, microsecs, lw=2, label='earth')
plt.legend(loc='upper left', shadow=False, fontsize='x-large')
plt.xscale('log')
plt.yscale('log')
plt.ylim(1E+02, 1E+06)

plt.savefig("jplephem speed test " + ephem.split('.')[0])

plt.show()



"""Vector functions and their composition."""

from numpy import max, min
from .constants import C_AUDAY
from .errors import DeprecationError, raise_error_for_deprecated_time_arguments
from .functions import length_of
from .positionlib import build_position
from .timelib import Time

class VectorFunction(object):
    """Given a time, computes a corresponding position."""

    ephemeris = None

    def __add__(self, other):
        if self.target != other.center:
            if other.target == self.center:
                self, other = other, self
            else:
                raise ValueError(
                    "you can only add two vectors"
                    " if the target where one of the vectors ends"
                    " is the center where the other vector starts"
                )

        selfp = getattr(self, 'positives', None) or (self,)
        selfn = getattr(self, 'negatives', ())

        otherp = getattr(other, 'positives', None) or (other,)
        othern = getattr(other, 'negatives', ())

        return VectorSum(self.center, other.target,
                         self.center_name, other.target_name,
                         selfp + otherp, selfn + othern)

    def __sub__(self, other):
        if self.center != other.center:
            raise ValueError(
                "you can only subtract two vectors"
                " if they both start at the same center"
            )

        selfp = getattr(self, 'positives', None) or (self,)
        selfn = getattr(self, 'negatives', ())

        otherp = getattr(other, 'positives', None) or (other,)
        othern = getattr(other, 'negatives', ())

        return VectorSum(other.target, self.target,
                         self.target_name, other.target_name,
                         selfp + othern, selfn + otherp)

    @raise_error_for_deprecated_time_arguments
    def at(self, t):
        """At time ``t``, compute the target's position relative to the center.

        If ``t`` is an array of times, then the returned position object
        will specify as many positions as there were times.  The kind of
        position returned depends on the value of the ``center``
        attribute:

        * Solar System Barycenter: :class:`~skyfield.positionlib.Barycentric`
        * Center of the Earth: :class:`~skyfield.positionlib.Geocentric`
        * Difference: :class:`~skyfield.positionlib.Geometric`
        * Anything else: :class:`~skyfield.positionlib.ICRF`

        """
        if not isinstance(t, Time):
            raise ValueError('please provide the at() method with a Time'
                             ' instance as its argument, instead of the'
                             ' value {0!r}'.format(t))
        observer_data = ObserverData()
        observer_data.ephemeris = self.ephemeris
        p, v, observer_data.gcrs_position, message = self._at(t)
        center = self.center
        if center == 0:
            observer_data.bcrs_position = p
            observer_data.bcrs_velocity = v
        self._snag_observer_data(observer_data, t)
        position = build_position(p, v, t, center, self.target, observer_data)
        position.message = message
        return position

    def _snag_observer_data(self, data, t):
        pass

    def _observe_from_bcrs(self, observer):
        assert self.center == 0
        return _correct_for_light_travel_time(observer, self)

    def geometry_of(self, other):
        raise DeprecationError(
"""the geometry_of() method has, alas, been deprecated

This old method has been replaced by an improved interface.  If you just
need your software working again, install Skyfield 0.9.1 for a quick fix:

    pip install skyfield==0.9.1

Or, to update your old code, replace each operation that looks like:

    position = boston.geometry_of(satellite).at(t)

with the vector math that was previously hiding inside the old method:

    position = (satellite - boston).at(t)""")

    def topos(self, latitude=None, longitude=None, latitude_degrees=None,
              longitude_degrees=None, elevation_m=0.0, x=0.0, y=0.0):
        raise DeprecationError(
"""the topos() method has, alas, been deprecated

This old method has been replaced by an improved interface.  If you just
need your software working again, install Skyfield 0.9.1 for a quick fix:

    pip install skyfield==0.9.1

Or, to update your old code, replace each operation that looks like:

    boston = earth.topos(...)

with the vector math that was previously hiding inside the old method:

    from skyfield.api import Topos
    boston = earth + Topos(...)""")

    def satellite(self, text):
        raise DeprecationError(
"""the satellite() method has, alas, been deprecated

This old method has been replaced by an improved interface.  If you just
need your software working again, install Skyfield 0.9.1 for a quick fix:

    pip install skyfield==0.9.1

Or, to update your old code, replace each operation that looks like:

    sat = earth.satellite(tle_text)

with the vector math (and the little bit of text manipulation) that was
previously hiding inside the old method:

    from skyfield.api import EarthSatellite
    line1, line2 = tle_text.splitlines()[-2:]
    sat = earth + EarthSatellite(line1, line2)""")


class VectorSum(VectorFunction):
    def __init__(self, center, target, center_name, target_name,
                 positives, negatives):
        self.center = center
        self.target = target
        self.center_name = center_name
        self.target_name = target_name
        self.positives = positives
        self.negatives = negatives

        # For now, just grab the first ephemeris we can find.
        ephemerides = (segment.ephemeris for segments in (positives, negatives)
                       for segment in segments if segment.ephemeris)
        self.ephemeris = next(ephemerides, None)

    def __str__(self):
        positives = self.positives
        negatives = self.negatives
        lines = [' - ' + str(segment) for segment in reversed(negatives)]
        lines.extend(' + ' + str(segment) for segment in positives)
        return 'Sum of {0} vectors:\n{1}'.format(
            len(positives) + len(negatives),
            '\n'.join(lines),
        )

    def __repr__(self):
        return '<{0} of {1} vectors {2} -> {3}>'.format(
            type(self).__name__,
            len(self.positives) + len(self.negatives),
            self.center_name,
            self.target_name,
        )

    def _at(self, t):
        p, v = 0.0, 0.0
        for segment in self.positives:
            p2, v2, gcrs_position, message = segment._at(t)
            p += p2
            v += v2
        for segment in self.negatives:
            p2, v2, gcrs_position, ignored_message = segment._at(t)
            p -= p2
            v -= v2
        return p, v, gcrs_position, message

    def _snag_observer_data(self, observer_data, t):
        if self.negatives:
            final_segment = self.negatives[-1]
        elif self.positives:
            final_segment = self.positives[-1]
        final_segment._snag_observer_data(observer_data, t)


def _correct_for_light_travel_time(observer, target):
    """Return a light-time corrected astrometric position and velocity.

    Given an `observer` that is a `Barycentric` position somewhere in
    the solar system, compute where in the sky they will see the body
    `target`, by computing the light-time between them and figuring out
    where `target` was back when the light was leaving it that is now
    reaching the eyes or instruments of the `observer`.

    """
    t = observer.t
    ts = t.ts
    cposition = observer.position.au
    cvelocity = observer.velocity.au_per_d
    tposition, tvelocity, gcrs_position, message = target._at(t)
    distance = length_of(tposition - cposition)
    light_time0 = 0.0
    t_tdb = t.tdb
    for i in range(10):
        light_time = distance / C_AUDAY
        delta = light_time - light_time0
        if -1e-12 < min(delta) and max(delta) < 1e-12:
            break
        t2 = ts.tdb(jd=t_tdb - light_time)
        tposition, tvelocity, gcrs_position, message = target._at(t2)
        distance = length_of(tposition - cposition)
        light_time0 = light_time
    else:
        raise ValueError('light-travel time failed to converge')
    return tposition - cposition, tvelocity - cvelocity, light_time


class ObserverData(object):
    """Essential facts about an observer, that may be needed later."""
    # TODO: expand the documentation for this class

    __slots__ = ('altaz_rotation', 'elevation_m', 'ephemeris',
                 'gcrs_position', 'bcrs_position', 'bcrs_velocity')

    def __init__(self):
        self.altaz_rotation = None
        self.elevation_m = None
        self.ephemeris = None
        self.gcrs_position = None
        self.bcrs_position = None
        self.bcrs_velocity = None

import sqlite3
import base64
conn = sqlite3.connect('snippet.db') 
c = conn.cursor()
conn.text_factory = str
file = """
# %load SearchFilename.py
'''
Search a filename for a phrase and how many following lines to display
USAGE:
import SearchFilename
filename = "hek.txt"
length = 4
SearchFilename.searchfilename(filename, length)
'''
def searchfilename(filename, length):
    f = open(filename, "r")
    searchlines = f.readlines()
    f.close()
    search = str(raw_input("Search Phrase : "))
    for i, line in enumerate(searchlines):
        if search in line: 
            for l in searchlines[i:i+length]: print l,
            print
            
#USAGE:
import SearchFilename
filename = "ALL_WIKI_GOOD.txt"
# length = how many lines after
length = 7
SearchFilename.searchfilename(filename, length) 
"""
keywords = "store, retrieve images, from SQLite Database"
encodedlistvalue=base64.b64encode(file)
c.execute("INSERT INTO snippet VALUES (?,?,?)", (encodedlistvalue, file, keywords))
conn.commit()
conn.close()



