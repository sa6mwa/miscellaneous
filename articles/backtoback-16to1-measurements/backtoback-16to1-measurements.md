# 16:1 transformer loss

**By [SA6MWA Michel Blomgren][qrz]**  
*sa6mwa@radiohorisont.se*  
*February 2020*

I have made several 16:1 transformers to be used with various broadband HF
antennas where the broadband feature is realized by terminating it with a
1000&#937; resistor. Configurations that I have experimented with over the
years include terminated folded dipoles (TFD or more commonly terminated tilted
folded dipole, T2FD), terminated rhombics and terminated delta loops.  Most
recently I favour [KQ6XA Bonnie Crystal's broadband butterfly terminated dipole][bbtd]
(BBTD) because of it's size when packed and easy installation. My modification
is to put both the transformer and resistor in the same box. This makes it
slightly less efficient since transformer and resistor wires are closer
together, but with the advantage of being really small when packed and even
easier to install.

My 16:1 transformers are all quadrifilar wound on Fair-Rite's 43 or 61 toroids.
For the lower end of HF, 1 to 10 MHz, I have found best results using 43
material (FT240-43 or FT140-43), while 61 material of the same 16:1 design is
better above 10 MHz. Both designs seem to work best with 6 turns quadrifilar
windings. Make it pretty, neat and tight with the 4 wires laying flat against
the toroid have made no significant measurable difference on my end compared to
twisting all the 4 wires together.

The measurements were made using a FT817 transceiver (at 5 watts), a MAAS power
meter and a dummy load. Two transformers were connected back-to-back, meaning
the FT817 was connected to one transformer (up 16 times) which was connected to
another 16:1 transformer (down 16 times) which in turn was connected using coax
to the power meter. The dummy load was connected to the power meters antenna
connector. The power meter is analog and it does not show correct values on all
bands, but this is reflected by the reference measurements (FT817 to power
meter to dummy load).

### The Math

The dB loss was calculated from the power ratio between the reference
measurement (in Watts) and the value with the two transformers in line using
10Log10. GNU ``bc`` was used for the calculations with the following
commands...

```console
$ bc -l
ratio=0.9
10*l(ratio)/l(10)
-.4573
```

The following function was defined to simplify the process...

```bc
define log10 (x) { return (10*l(x)/l(10)); }
log10(0.5)
-3.0102

log10(0.6/3.5)
-7.6599
```

### Loss through two 16:1 transformers

Two 16 to 1 transformers were connected back-to-back, each transformer had 6
turns quadrifilar windings on an FT140-43 toroid (43 material).

| QRG kHz | Reference (Watts) | Back to back 16:1 (W) | dB    | Loss dB/2 |
|--------:|------------------:|----------------------:|------:|----------:|
| 1800    | 3.75              | 3.4                   | 0.43  | 0.213     |
| 2500    | 4.4               | 3.9                   | 0.524 | 0.262     |
| 3000    | 4.6               | 4.1                   | 0.495 | 0.25      |
| 3500    | 4.75              | 4.3                   | 0.432 | 0.216     |
| 4000    | 4.8               | 4.4                   | 0.378 | 0.189     |
| 5000    | 4.9               | 4.3                   | 0.567 | 0.283     |
| 6000    | 5.0               | 4.3                   | 0.655 | 0.327     |
| 7000    | 5.0               | 4.3                   | 0.655 | 0.327     |
| 10100   | 5.0               | 4.1                   | 0.862 | 0.431     |
| 14000   | 5.0               | 3.8                   | 1.192 | 0.596     |
| 18068   | 5.0               | 3.6                   | 1.427 | 0.713     |
| 28000   | 5.1               | 2.25                  | 3.554 | 1.777     |
| 50000   | 4.6               | 0.25                  | 12.65 | 6.324     |

The *dB* column is the ratio between reference and back-to-back through two
transformers. Loss through one transformer is assumed to be dB/2.

The lowest loss was at 4 MHz, but generally very similar low loss from 1 to 5
MHz and below 0.5 dB loss up to about 11 MHz, meaning it is an excellent NVIS
(near vertical incidence skywave) transformer for higher latitudes (where foF2
is almost never above 7 MHz), especially during winter in solar minimum when
foF2 can be below 3 MHz for several weeks.

![Gnuplot 16:1 transformer loss][svgxfrmrloss]

[Gnuplot 16:1 transformer loss][gpixfrmrloss]

## Conclusion

A 16:1 transformer constructed on a FT140-43 toroid using 6 quadrifilar turns
has good efficiency between about 1 to 11 MHz which makes it an excellent
choice for high latitude NVIS operation using broadband (tuner-less) resistor
terminated antennas (for example a broadband butterfly or folded dipole
terminated with a 1000&#937; resistor).

``73 DE SA6MWA +``

[qrz]: https://www.qrz.com/db/SA6MWA
[outsender]: https://www.youtube.com/c/utesandaren
[bbtd]: http://hflink.com/antenna/
[svgxfrmrloss]: tl-transformer-16to1.svg
[gpixfrmrloss]: tl-transformer-16to1.gpi
