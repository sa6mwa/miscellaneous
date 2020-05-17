#!/usr/bin/python
import sys

fpp = 3 # floating point precision

feet_in_meters = 1200.0/3937.0

df = 142.65 # 143
invvf = 137.16 # 138

mhz = 0.0

# (468/3.5)*(1200/3937)
# (450/3.5)*(1200/3937)

def usage():
  print "usage: {me} MHz".format(me=sys.argv[0])
  sys.exit(1)


if len(sys.argv) == 2:
  mhz = sys.argv[1]
else:
  usage()

mhz = float(mhz)

hw = 300 / mhz / 2
hw_dipole = df / mhz
hw_invv = invvf / mhz

print """QRG MHz | Half wave (300/f MHz/2) | HW dipole formula (143/f Mhz) | HW inv.V formula (138/f MHz)
--------+-------------------------+-------------------------------+-----------------------------"""
for m in range(1, 16):
  nf = mhz * float(m)
  hw = 300 / nf / 2
  hw_dipole = df / nf
  hw_invv = invvf / nf
  print "{nf:7} | {hw:23} | {hw_dipole:29} | {hw_invv:28}".format(nf=round(nf, fpp), hw=round(hw, fpp), hw_dipole=round(hw_dipole, fpp), hw_invv=round(hw_invv, fpp))

