#!/usr/bin/python2
# slimjim and j pole calculator by sa6mwa@radiohorisont.se
# inspired by m0ukd's js calculator:
# https://m0ukd.com/calculators/slim-jim-and-j-pole-calculator/
import sys

# default velocity factor of ladder line (vfl)
vfl = 0.957
# default velocity factor of radiating element (if not the same ladder line)
vfr = 0.957
# 450 ohm ladder line, vf = 0.91
# bare copper pipe, vf = 0.96
# 1.5mm2 black RKUB, vf = 0.94
floating_point_precision = 2

# choke array = [from_mhz, to_mhz, rg58 turns on form, form mm]
chokes = [  [25,30,5,110], [20,25,7,110], [15,20,10,110], [11,15,15,110], [8,14,20,110], [7,13.5,25,110] ]


def usage():
  print """usage: {me} mhz [velocity_factor]
example with default vf: {me} 144.600
slimjim example using ladder line with 96% vf: {me} 50.05 0.96
jpole with different vf for 1/2 wave and 1/4 wave sections: {me} 145.5 0.91 0.89""".format(me=sys.argv[0])
  sys.exit(1)

if len(sys.argv) < 2:
  usage()

if len(sys.argv) == 2:
  frequency = sys.argv[1]
elif len(sys.argv) == 3:
  frequency = sys.argv[1]
  vfl = sys.argv[2]
  vfr = vfl
elif len(sys.argv) == 4:
  frequency = sys.argv[1]
  vfl = sys.argv[2]
  vfr = sys.argv[3]
else:
  usage()

frequency = float(frequency)
vfl = float(vfl)
vfr = float(vfr)

aslimjim = round(22500*vfl/frequency+300/frequency, floating_point_precision)
#ajpole = round(30000*(0.75*vf)/frequency, floating_point_precision)
ajpole = round((30000*(0.5*vfr)/frequency) + (30000*(0.25*vfl)/frequency), floating_point_precision)
b = round(30000*(0.5*vfl)/frequency, floating_point_precision)
c = round(30000*(0.25*vfl)/frequency, floating_point_precision)
d = round(30000*(0.025*vfl)/frequency, floating_point_precision)
e = round(300/frequency, floating_point_precision)
f = round(30000*0.02175/frequency, floating_point_precision)

qwl = round((c*2)+f, floating_point_precision)
hwl = b
pipelength = round(qwl + hwl, floating_point_precision)

print """
G2BCX SLIM JIM FOR {} MHz
Velocity factor for radiating 1/2 wave = {}
Velocity factor for 1/4 wave stub = {}
          .---.                   .
          |<F>|                   | J POLE VERSION
          |   |                   | (ignore E, AJ = AS-E or B+C)
          |   |B (1/2 wave)       |
          |   |                   | B (1/2 wave element)
       AS |   |                   | AJ (overall length)
 (overall |   |                   |
  length) |     E (gap = A-B-C)   |
          |   |                   |   |
          |   |C (1/4 wave)       |   | C (1/4 wave)
          L D S                   L D S
          | | |                   | | |
          '-|-'                   '-|-'
            | D=50 ohm feed point   |
            O <-- RF choke          O
            |                       |
  L = lead, inner conductor of coax
  S = shield of coax
  D = length from bottom where to solder L and S (match point)

  AS = {} cm              AJ = {} cm
  B = {} cm
  C = {} cm
  D = {} cm
  E = {} cm
  F = {} cm (not critical, can be ignored, works anyway)

  Pipe/wire total length = {} cm
  Quarter wave material length = {} cm
  Half wave material length = {} cm
""".format(frequency, vfr, vfl, aslimjim, ajpole, b, c, d, e, f, pipelength, qwl, hwl)


#SLIMJIM HOW TO USING 450 OHM LADDER LINE
#Make sure you have the full length of A. Start measuring B from the top.
#Continue further to make sure that the gap E fits within a solid portion of the
#ladder line (will ensure it hangs correctly and is more durable). After the
#gap, measure C. Leave approx 5 cm and cut. Strip the ends and create some way
#to adjust the length of C, e.g by zip-tying each end of the bare wire to each
#other or twist the ends together starting at the calculated length of C. You
#tune primarily by adjusting the length of C, but may also require to adjust D.
#You should not need to adjust B or E. Measure B from gap and cut 1-1.5 cm
#further, strip, twist and solder together. Strip 1-3 cm of insulation from both
#wires at the matching point D. Make holes in ladder line and fix coax, strip it
#and solder to D.
