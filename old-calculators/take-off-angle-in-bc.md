# Take-Off-Angle (TOA) in GNU bc

Below, function toa() is provided to calculate incidence angle into the
ionosphere for a certain distance using GNU `bc` (binary calculator). BC has to
be executed with `-l` or `--mathlib`. Usage is `toa(distance_in_km,
height_of_ionospheric_layer)`. You need to provide `hmF2` or `hmE`, `hmF1`, etc
as height. You probably want `hmF2`. `hmF2` is the altitude of the peak
density of the F2 layer. It will not reflect *true* true height of
reflection/refraction, but close enough, and is what you can get from an
ionogram such as one from Lowell's 4D Digisonde.

Example:
```
$ bc -l
define toa(distance, hmf2) {
  scale=10
  pi=4*a(1)
  earthradius=40000/2/pi
  earthanglea=distance/40000*(2*pi)
  horizontal=earthradius*s(earthanglea/2)
  tangentvalue=(pi-earthanglea/2)/2
  vertical=horizontal/(s(tangentvalue)/c(tangentvalue))
  takeoffangle=a((vertical+hmf2)/horizontal)-earthanglea/2
  takeoffangledegrees=takeoffangle/pi*180
  return takeoffangledegrees
}
toa(100, 189)
74.7467011080
```

The angle of incidence is almost 75 degrees, meaning your antenna ought to have
it's gain in this part of the radiation pattern for this link (100 km).

Math adapted from OH1TV Pekka's *TOA MUF calculator.xls* Excel spreadsheet
found here <http://www.kolumbus.fi/pekka.ketonen/TOA%20MUF%20calculator.xls>.

The `mufd()` function can be used to calculate maximum usable frequency for the
distance if you also have the foF2 value from an ionogram. If
foF2 (vertical incidence, critical frequency, where no radar echo returns to
the ionosonde) is 4.3 MHz, mufd() can give us an indication where we still could
use the ordinary mode (O mode, as foF2 is ordinary mode) for the distance.
`mufd(100, 189, 4.3)` produces 4.45 MHz, i.e, in theory, MUF is slightly higher
than foF2 for this link (100 km) depending on the lower incidence (reflection
angle). toa(), foF2 and fxI are more important than MUF for communication
within a 200 km radius.

The functions...
```
define toa(distance, hmf2) {
  scale=10
  pi=4*a(1)
  earthradius=40000/2/pi
  earthanglea=distance/40000*(2*pi)
  horizontal=earthradius*s(earthanglea/2)
  tangentvalue=(pi-earthanglea/2)/2
  vertical=horizontal/(s(tangentvalue)/c(tangentvalue))
  takeoffangle=a((vertical+hmf2)/horizontal)-earthanglea/2
  takeoffangledegrees=takeoffangle/pi*180
  return takeoffangledegrees
}

define mufd(distance, hmf2, fof2) {
  scale=10
  pi=4*a(1)
  earthradius=40000/2/pi
  earthanglea=distance/40000*(2*pi)
  horizontal=earthradius*s(earthanglea/2)
  tangentvalue=(pi-earthanglea/2)/2
  vertical=horizontal/(s(tangentvalue)/c(tangentvalue))
  mufangle=a(horizontal/(vertical+hmf2))
  muffactor=1/c(mufangle)
  mufd=muffactor*fof2
  return mufd
}
```

# Take-Off-Angle to aerial receiver (signal reconnaissance aircraft)

Similar to the TOA function above, but distance is from the transmitter to the
aircraft in km and hmf2 is the aircraft's altitude in km. Add about 100 km to 0
degree result for 2 to 3 MHz ground wave coverage given that antenna is high in
the open or a vertical antenna in flat terrain. 160m ground wave coverage with
a vertical antenna could be 150 km depending on terrain and power. For
signature adapted NVIS (the Zenith Concept) consider everything below 10
degrees not received as ground, surface or direct wave at all (10 degrees
includes margin for defraction and ground wave coverage).

```
define toasr(distance, altitude) {
  scale=10
  pi=4*a(1)
  earthradius=40000/2/pi
  earthanglea=(distance*2)/40000*(2*pi)
  horizontal=earthradius*s(earthanglea/2)
  tangentvalue=(pi-earthanglea/2)/2
  vertical=horizontal/(s(tangentvalue)/c(tangentvalue))
  takeoffangle=a((vertical+altitude)/horizontal)-earthanglea/2
  takeoffangledegrees=takeoffangle/pi*180
  return takeoffangledegrees
}
```

Some results...
```
$ bc -l
# 406 km from aircraft at 13000m to transmitter
toasr(406, 13)
.0044774280
# 0 degrees
# Add 100 km for ground wave coverage for low HF = 506 km
# Maximum non-skywave reception range (i.e ground or direct wave) over flat
# terrain is 506 km.

toasr(252, 5)
.0020774700
# 0 degrees, add 100 km gnd wave for low HF = 352 km
# Maximum non-skywave reception range for aircraft at 5000m is 352 km,
# possibly maximum 402 km if listening on 160m

toasr(70, 13)
10.1951891820
# 10.2 degrees take-off-angle.
# This should be more than enough to avoid exposing your direct or ground wave
# to this aircraft (at 13000m) when it's 70 km away.
```

Reference:

<https://www.researchgate.net/publication/263054262_Near_Vertical_Incidence_Skywave_Propagation_Elevation_Angles_and_Optimum_Antenna_Height_for_Horizontal_Dipole_Antennas>
