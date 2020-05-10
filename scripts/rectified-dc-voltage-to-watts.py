#!/usr/bin/python
import sys
import math

fvd = 0.2 # forward voltage drop (across the diode)
fpp = 2 # floating point precision
#rms = 0.70710678 # rms multiplier = 1/sqrt(2)
rms = 1.0/math.sqrt(2)
dcv_loaded = 0.0
dcv_unloaded = 0.0
rms_loaded = 0.0
rms_unloaded = 0.0
r = 0.0
z = 50.0

def usage():
  print """For use with an RF to DC rectifier circuit, e.g:
http://www.zen22142.zen.co.uk/Circuits/Testgear/rfprobe.htm

usage:
{me} dcV_loaded [impedance_in_ohms || dcV_unloaded load_in_ohms]

examples:
# 22.35 V DC is 5 Watts when the impedance is 50 Ohm:
{me} 22.35

# 22.35 V DC is 5.55 Watts with an impedance of 45 Ohm:
{me} 22.35 45

# 22.35 VDC with a 50 Ohm load, but 42.5 VDC without a load,
# that makes the impedance of the transmitter 45.08 Ohms and
# the output power 5.54 Watts:
{me} 22.35 42.5 50
""".format(me=sys.argv[0])
  sys.exit(1)

if len(sys.argv) == 2:
  dcv_loaded = sys.argv[1]
elif len(sys.argv) == 3:
  dcv_loaded = sys.argv[1]
  z = sys.argv[2]
elif len(sys.argv) == 4:
  dcv_loaded = sys.argv[1]
  dcv_unloaded = sys.argv[2]
  r = sys.argv[3]
else:
  usage()

dcv_loaded = float(dcv_loaded)
dcv_unloaded = float(dcv_unloaded)
r = float(r)
z = float(z)

if dcv_unloaded > 0.0 and r < 10.0:
  usage()
if dcv_unloaded > 0.0 and dcv_unloaded < 0.5:
  usage()
if dcv_loaded < 0.5:
  usage()

print "Forward voltage drop (V) = {fvd}".format(fvd=round(fvd, fpp))
print "Loaded peak voltage (V) = {dcv_loaded}".format(dcv_loaded=round(dcv_loaded, fpp))
rms_loaded = (dcv_loaded + fvd) * rms
print "Loaded RMS voltage (V) = {rms_loaded}".format(rms_loaded=round(rms_loaded, fpp))

if dcv_unloaded > 0:
  print "Unloaded peak voltage (V) = {dcv_unloaded}".format(dcv_unloaded=round(dcv_unloaded, fpp))
  rms_unloaded = (dcv_unloaded + fvd) * rms
  print "Unloaded RMS voltage (V) = {rms_unloaded}".format(rms_unloaded=round(rms_unloaded, fpp))
  # calculate impedance
  z = (r * (rms_unloaded - rms_loaded)) / rms_loaded
  if z == 0:
    print "ERROR: impedance can not be 0"
    sys.exit(1)

print "Impedance (Z in Ohm) = {z}".format(z=round(z, fpp))

pwr = (rms_loaded ** 2.0) / z

print "Power (Watts) = {pwr}".format(pwr=round(pwr, fpp))


w5v = round(math.sqrt(5.0 * z) / rms - fvd, fpp)
w3v = round(math.sqrt(3.0 * z) / rms - fvd, fpp)
w1v = round(math.sqrt(1.0 * z) / rms - fvd, fpp)
w0v5 = round(math.sqrt(0.5 * z) / rms - fvd, fpp)

print """
CHEAT-SHEET PEAK VOLTAGE FOR PREDEFINED POWER LEVELS
  5W peak voltage = {w5v}
  3W peak voltage = {w3v}
  1W peak voltage = {w1v}
  0.5W peak voltage = {w0v5}
""".format(w5v=w5v, w3v=w3v, w1v=w1v, w0v5=w0v5)
