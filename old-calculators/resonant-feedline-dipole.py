#!/usr/bin/python2
# resonant feedline dipole (RFD) calculator
import sys
# default velocity factor (vf)
vfl = 0.96 # vf of insulated copper wire
vfs = 0.96 # to center of coil
vfc = 0.66 # vf of coax

floating_point_precision = 2
# speed of light to get centimeter in the calculation below
dividend = 299792458*0.0001

def usage():
  print """usage: {me} mhz [velocity_factor_lead] [velocity_factor_shield] [velocity_factor_coax]
example with default vf: {me} 14.1
{me} 27.2 0.97""".format(me=sys.argv[0])
  sys.exit(1)

if len(sys.argv) < 2:
  usage()

if len(sys.argv) == 2:
  frequency = sys.argv[1]
elif len(sys.argv) == 3:
  frequency = sys.argv[1]
  vfl = sys.argv[2]
  vfs = vfl
elif len(sys.argv) == 4:
  frequency = sys.argv[1]
  vfl = sys.argv[2]
  vfs = sys.argv[3]
elif len(sys.argv) == 5:
  frequency = sys.argv[1]
  vfl = sys.argv[2]
  vfs = sys.argv[3]
  vfc = sys.argv[4]
else:
  usage()

frequency = float(frequency)
vfl = float(vfl)
vfs = float(vfs)
vfc = float(vfc)

a = round(dividend*(0.25*vfl)/frequency, floating_point_precision)
b = round(dividend*(0.25*vfs)/frequency, floating_point_precision)
c = round(dividend*(0.5*vfc)/frequency, floating_point_precision)
tot = a + b

print """
RESONANT FEEDLINE DIPOLE (RFD) FOR {} MHz
Total length = {} cm
                    coax to center
                    of coil {} cm vf={}
                                        lead {} cm vf={}
    ===============()===================---------------------
        ^          ^
        |          |
        |    Common Mode Choke, see
        | http://www.karinya.net/g3txq/chokes/
        |
    1/2 wave length coax for minimum common mode current:
    coax length = {} cm (vf={})
    2 * hwl = {} m
    3 * hwl = {} m
    5 * hwl = {} m
    11 * hwl = {} m
    13 * hwl = {} m
    19 * hwl = {} m
    20 * hwl = {} m
""".format(frequency, tot, b, vfs, a, vfl, c, vfc,
  round(c*2/100, floating_point_precision),
  round(c*3/100, floating_point_precision),
  round(c*5/100, floating_point_precision),
  round(c*9/100, floating_point_precision),
  round(c*11/100, floating_point_precision),
  round(c*13/100, floating_point_precision),
  round(c*19/100, floating_point_precision),
  round(c*20/100, floating_point_precision)
  )

