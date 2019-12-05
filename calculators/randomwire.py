#!/usr/bin/python

feet1 = [ 29, 35.5, 41, 58, 71, 84, 107, 119, 148, 203, 347, 407, 423 ]
feet2 = [ 53, 59, 72, 88.5, 98.5, 124.5, 135, 146, 162, 175 ]
feet3 = [ 53, 124.5 ]
feet4 = [ 58, 71, 84, 107, 119, 148, 203 ]
all_feets = feet1 + feet2 + feet3 + feet4

counterpoise = [ 30, 40 ]
one_feet_in_mm = 304.8

print "long wire lengths\nhttp://www.hamuniverse.com/randomwireantennalengths.html"
for x in feet1:
  meter = round(x * one_feet_in_mm / 1000.0, 4)
  print "{} meters ({} feet)".format(meter, x)
print "good for 80-40-30-20-17-15-12-10 meters = 32.6136 meters (107 feet) or 21.6408 meters (71 feet)"

print "\nend-fed with 9:1 unun according to balundesigns\nhttps://www.balundesigns.com/content/Wire%20Lengths%20for%204%20and%209-1%20ununs.pdf"
for x in feet2:
  meter = round(x * one_feet_in_mm / 1000.0, 4)
  print "{} meters ({} feet)".format(meter, x)

print "\nrecommended for end-fed with 9:1 unun according to balundesigns"
for x in feet3:
  meter = round(x * one_feet_in_mm / 1000.0, 4)
  print "{} meters ({} feet)".format(meter, x)

print "\nalternatives for 4:1 and 9:1 ununs"
for x in feet4:
  meter = round(x * one_feet_in_mm / 1000.0, 4)
  print "{} meters ({} feet)".format(meter, x)

print "\ncounterpoise lengths for 9:1 unun end-feds"
for x in counterpoise:
  meter = round(x * one_feet_in_mm / 1000.0, 4)
  print "{} meters ({} feet)".format(meter, x)


print "\nall feets:"
for x in all_feets:
  meter = round(x * one_feet_in_mm / 1000.0, 4)
  print meter

