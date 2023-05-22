#!/usr/bin/python2
# 4:1 off center fed dipole calculator
import sys
# default end effect compensation ratio (aka velocity factor)
# ratio = 0.952
ratio = 0.96
#shortleg = 0.36/2.0
#longleg = 0.64/2.0
#shortleg = 0.33333333/2.0
#longleg = 0.66666666/2.0
shortleg = (1.0/3)/2.0
longleg = (2.0/3)/2.0
floating_point_precision = 2
# speed of light to get meters in the calculation below
dividend = 299792458*0.001


def usage():
  print """usage: {me} khz [end_effect_ratio_velocity_factor]
80-10m ocf with default vf: {me} 3580
40-10m ocf with default vf: {me} 7040""".format(me=sys.argv[0])
  sys.exit(1)

if len(sys.argv) < 2:
  usage()

if len(sys.argv) == 2:
  frequency = sys.argv[1]
elif len(sys.argv) == 3:
  frequency = sys.argv[1]
  ratio = sys.argv[2]
else:
  usage()

frequency = float(frequency)
ratio = float(ratio)

a = round(dividend*(shortleg*ratio)/(frequency), floating_point_precision)
b = round(dividend*(longleg*ratio)/(frequency), floating_point_precision)
tot = a + b

print """
OCF DIPOLE FOR {qrg} kHz
Total length = {tot} m

       short end = {shrt} m          radiating = {lng} m
          (ee={ratio})                    (ee={ratio})
    -------------------- -------------------------------------
                        | 4:1 voltage or current balun @ feedpoint
                        |
                        |
                        |
""".format(qrg=int(frequency), tot=tot, shrt=a, lng=b, ratio=ratio)
