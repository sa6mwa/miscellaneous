# Signature Managed Upper Frequency (SMUF)

According to [Design and Validation of Probes and Sensors for the
Characterization of Magneto-Ionic Radio Wave Propagation on Near Vertical
Incidence Skywave Paths](https://www.mdpi.com/1424-8220/19/11/2616/htm) fxF2
(layer F2 critical frequency of the extraordinary wave) can be simplified as
being 0.55 MHz above foF2 (the F2 layer critical frequency of the ordinary
wave) in the northern hemisphere at mid-european latitudes. This is obviously a
simplification, but is at least a number taken from a published scientific
article.

According to the paper [Predictions of HF system performance for propagation
through disturbed ionospheres measured using low-Earth-orbit satellite radio
beacon
tomography](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014RS005409)
90% of foF2 resulted in that absolutely vertical incidence rays penetrated the
ionosphere and was picked up by an overhead satellite. In figure 4 of this
article you notice that only the ordinary wave (O mode) escaped the ionosphere
into space. The extraordinary rays (X) all remained within the ionosphere and
could not be picked up by the satellite. Although the satellite need to be
precisely overhead to pick up this signal and direction finding is extremely
coarse, is there a way to prevent the ray from escaping into outer space?

## The theory of signature reducing NVIS satellite interception

My theory is that 90% of foF2 is too high of a frequency if your goal is radio
signature management and prevent interception by an overhead satellite. You can
always communicate vertically (NVIS) above foF2 as long as you are below fxI
(or fxF2, the critical frequency of the extraordinary wave in the F2 layer). As
can be seen in figure 4, the extraordinary rays cover the entire NVIS converage
area, not the O-mode. For optimal transmission, you want to use the O-mode for
better efficiency and much better signal-to-noise ratio on low power. Thus, 90%
of foF2 appears to be too high for NVIS and certainly too high to prevent the
ordinary wave to penetrate the ionosphere.

Although untested, but based on these two papers, I choose to operate on 90% of
foF2 minus 550 kHz. Below is a function in GNU binary calculator (`bc`) to
obtain this new *signature managed upper frequency* (SMUF).

```
define smuf(fof2) { scale=3 ; return fof2*((fof2*0.9)-0.55)/fof2 }
```

Example:

```
# foF2 according to ionogram from a nearby ionosonde says 5.1 MHz
smuf(5.1)
4.040
# you set the VFO on your transceiver to your first assigned QRG below 4.04 MHz

# night time low foF2, e.g. higher latitudes during winter
smuf(2.4)
1.610
```

The above example of an foF2 at 2.4 MHz means that an foF2 of 2.4 is about as
low as you can go to safely avoid satellite interception (according to the
theory herein) as most modern *military* transceivers (Hughes, etc) do not
transmit below 1.6 MHz. Antenna efficiency is also problematic as height above
ground need to be up towards 30 meters to overcome high ground losses and a
half wave dipole is about 90 meters on 1.6 MHz. A 30 meter terminated folded
dipole will not work very well.
