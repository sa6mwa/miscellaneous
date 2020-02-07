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
  tangentvalue=(pi-eaa/2)/2
  vertical=horizontal/(s(tangentvalue)/c(tangentvalue))
  takeoffangle=a((vertical+hmf2)/horizontal)-earthanglea/2
  takeoffangledegrees=takeoffangle/pi*180
  return takeoffangledegrees
}
toa(100, 189)
74.7319985460
```

So, NVIS (near vertical incidence skywave) and the angle of incidence is almost
75 degrees, meaning you antenna ought to have it's gain in this part of the
radiation pattern for this link (100 km).

Math adapted from OH1TV Pekka's *TOA MUF calculator.xls* Excel spreadsheet
found somewhere on the internet.

The `mufd()` function can be used to calculate maximal usable frequency for the
distance if you also have the foF2 value from the ionogram. For example, if
foF2 (vertical incidence, critical frequency, where no radar echo returns to
the ionosonde) is 4.3 MHz mufd() can give us an indication where we still could
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
  tangentvalue=(pi-eaa/2)/2
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
  tangentvalue=(pi-eaa/2)/2
  vertical=horizontal/(s(tangentvalue)/c(tangentvalue))
  mufangle=a(horizontal/(vertical+hmf2))
  muffactor=1/c(mufangle)
  mufd=muffactor*fof2
  return mufd
}
```

Reference:

<https://www.researchgate.net/publication/263054262_Near_Vertical_Incidence_Skywave_Propagation_Elevation_Angles_and_Optimum_Antenna_Height_for_Horizontal_Dipole_Antennas>
