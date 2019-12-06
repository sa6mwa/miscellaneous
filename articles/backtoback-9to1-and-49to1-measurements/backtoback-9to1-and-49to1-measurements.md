# 9:1 and 49:1 transformer loss

**By [SA6MWA Michel Blomgren][qrz]**  
*sa6mwa@radiohorisont.se*  
*December 2019*

I wanted to measure the loss through two types of transformers I have made
myself: the very popular 49:1 used for End-Fed Half Wave (EFHW) antennas and
the popular, but sometimes maligned, 9:1 *unun* used for *random wire* or long
wire antennas. On my YouTube channel [Utesändaren][outsender] (which is in
Swedish) I have tried to debunk the pseudo-science floating around on the net
about the inefficiency of end-fed, non-resonant wires and take the scientific
standpoint that all wires are equally efficient whether they are fed in the
middle or by the end (given the same length) provided that you can match the
impedance.

Another misconception floating around is that the popular 49:1 (14 secondary
windings, 2 primary windings on a FT240-43 or FT140-43) is a highly efficient
transformer. Since I don't own a VNA, I decided to measure TL (transmission
loss, or sometimes called thru-loss) through 2 transformers back-to-back using
a simple power meter connected to a dummy load using an ordinary transceiver.

Transmission Loss was measured using a FT817 at 5W CW. The first measurements
were for reference and connected the FT817 directly to a MAAS RS600
power/swr-meter via a 200mm RG58 lead (with PL259 bakelite connectors). The ANT
connection on the RS600 had a homemade dummyload connected directly via N and
UHF adapters. The dummy load consisted of a set of 1% 3W resistors in parallel
(50 ohm).

> Unknowingly my FT817 seem to produce low HI RF PWR on 160m (only 3.5W
> according to the power meter). The hidden menu of my FT817 (pressing A+B+C
> when powering on) shows ``24 HF1-HI`` set to ``98`` (160m RF PWR). It might
> be set too low or the power meter does not handle 160m very well. This might
> have affected the 160m results.

The second measurements were done by connecting the FT817 via the 200mm patch
lead to one of the transformer's SO239 sockets. Two 9 to 1 transformers were
connected together, including ground (using the transformer's ground plugs).
The antenna wire connector was connected to the other transformer's antenna
wire connector using a 50mm insulated copper wire. The ground of both
transformers were also connected together in the same way, with about 50mm of
insulated copper wire.

The transformers were two 9:1 trifilar-design wound 6 times on FT140-61
torroids each (1 torroid per transformer). The wire in both transformers were
what we call FK cable, single strand from an electric installation cable,
supposedly with PVC and some fire resistant insulation. None of the
transformers used more ideal enamel wire.

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

### Loss through two 9:1 transformers

| QRG kHz | Reference (Watts) | Back to back 9:1 (W)  | dB    | Loss dB/2 |
|--------:|------------------:|----------------------:|------:|----------:|
| 1800    | 3.5               | 1.1                   | 5.03  | 2.52      |
| 3500    | 4.6               | 3.7                   | 0.946 | 0.473     |
| 7000    | 4.9               | 4.8                   | 0.09  | 0.045     |
| 10100   | 5.0               | 5.0                   | 0     | 0         |
| 14000   | 5.0               | 4.8                   | 0.177 | 0.089     |
| 18068   | 5.0               | 4.725                 | 0.246 | 0.123     |
| 28000   | 5.1               | 4.6                   | 0.448 | 0.224     |
| 50000   | 4.6               | 3.5                   | 1.187 | 0.5935    |

The *dB* column is the ratio between reference and back-to-back through two
transformers. Loss through one transformer is assumed to be dB/2.

The lowest loss was at 30m where I could not detect a difference in position of
the needle compared to reference on the power meter. The highest loss was at
160m with a loss of 2.52 dB. On 80m it was below 0.5 and above 80 it was below
0.3.

### 49:1 back to back

Two 49:1 transformers

| QRG kHz | Reference (Watts) | Back to back 49:1 (W) | dB    | Loss dB/2 |
|--------:|------------------:|----------------------:|------:|----------:|
| 1800    | 3.5               | 0.6                   | 7.66  | 3.83      |
| 3500    | 4.6               | 1.8                   | 4.07  | 2.035     |
| 7000    | 4.9               | 2.5                   | 2.92  | 1.46      |
| 10100   | 5.0               | 2.725                 | 2.64  | 1.32      |
| 14000   | 5.0               | 2.8                   | 2.52  | 1.26      |
| 18068   | 5.0               | 2.8                   | 2.52  | 1.26      |
| 28000   | 5.1               | 2.25                  | 3.55  | 1.775     |
| 50000   | 4.6               | 0.3                   | 11.86 | 5.9287    |

The lowest loss was at 20m and 17m with a loss of 1.26 dB. The highest loss on
HF was at 160m with a loss of 3.83 dB, meaning more than half the power (58.6%)
is lost in the transformer. At 80m loss was below 3 dB, but still 40% of
transmitted power was lost in the transformer. At 40m through 10m the losses
are decent around 25-30%. 75% is lost as heat in the transformer at 6m, but VHF
was never really a design goal of this type of transformer.

![Gnuplot 9:1 vs 49:1 transformer loss][svgxfrmrloss]

[Gnuplot file of transformer loss][gpixfrmrloss]

## 9:1 system loss

Since a 9:1 *random wire* requires an ATU (antenna tuner) and you usually have a
relatively high SWR in the coax - does that combined loss make the 9:1 total
system loss worse than a matched 49:1 end-fed half-wave?

Even though the 49:1 was OK between 40m and 17m, it was nowhere near as good as
the 9:1 in the same range (near 0 dB loss). You need to use an antenna tuner
(impedance matching device) with a 9:1 *random wire* installation and there
will be SWR loss in the coax (unless using an external rugged ATU at the feed
point) and some loss in the impedance matching device.

### Transmission line loss

We begin with the transmission line. I use RG-58 when operating portable, so
let's see what the losses are in this type of coax. All numbers were derived
from [CO8TW Coax Calculator][coaxcalculator] on qsl.net.

Belden 8219 (RG58A) was chosen as the cable with lengths of 10 and 30 meters.
It's uncommon to feed end-fed antennas with a long run of coax, especially when
portable, as the transformer is usually not mounted high. I personally never
use more than 5-7 meters of coax (RG-58), unless it is a horizontal dipole.
This still allows me to get the transformer up a few meters in the air just
above my operating position.

A 9:1 *random wire* installation usually never result in a SWR of more than
5:1, usually a lot less. An end-fed resonant half-wave wire will typically have
an impedance no more than 3000 ohms (reference needed). 3000 divided by 9 is
333 ohms, divided by 50 is a SWR of 6.66 to 1. This will be or be near the
highest possible impedance in a typical random wire installation. When mounting
a random wire or end-fed half-wave as a sloper and relatively close to ground
(vs operating frequency), impedance is usually much lower resulting in a SWR of
less than 5:1 and mostly less than 3:1 with the 9:1 transformer. The same
installation makes it possible to use the 49:1 transformer with true half-wave
wires.

SWR losses for 10m coax...

| QRG kHz   | 10m SWR 1:1 total loss  | 10m SWR 5:1 total loss  |
|----------:|------------------------:|------------------------:|
| 1800      | 0.174                   | 0.434                   |
| 3500      | 0.245                   | 0.6                     |
| 7000      | 0.35                    | 0.839                   |
| 10100     | 0.424                   | 0.999                   |
| 14000     | 0.503                   | 1.167                   |
| 18068     | 0.575                   | 1.316                   |
| 28000     | 0.726                   | 1.616                   |
| 50000     | 0.994                   | 2.112                   |

SWR losses for 30m coax...

| QRG kHz   | 30m SWR 1:1 total loss  | 30m SWR 5:1 total loss  |
|----------:|------------------------:|------------------------:|
| 1800      | 0.523                   | 1.209                   |
| 3500      | 0.734                   | 1.632                   |
| 7000      | 1.05                    | 2.212                   |
| 10100     | 1.271                   | 2.588                   |
| 14000     | 1.508                   | 2.97                    |
| 18068     | 1.725                   | 3.304                   |
| 28000     | 2.178                   | 3.958                   |
| 50000     | 2.981                   | 5.014                   | 

#### My own measurements

The following data was acquired by measuring 7.5m and 30m respectively of
Lappkabel RG-58C/U mfg number 2170000 using the same method as with the
transformers: FT817 as a signal generator and a MAAS RS600 power meter with a
home-made dummy load.

| QRG kHz   | Ref (W) | 7.5m RG58 (W) | TL7m dB | 30m RG58 (W)  | TL30m dB  |
|----------:|--------:|--------------:|--------:|--------------:|----------:|
| 1800      | 3.5     | 3.5           | 0       | 3.4           | 0.126     |
| 3500      | 4.6     | 4.5           | 0.096   | 3.9           | 0.717     |
| 7000      | 4.9     | 4.6           | 0.275   | 3.8           | 1.104     |
| 10100     | 5.0     | 4.6           | 0.362   | 3.6           | 1.427     |
| 14000     | 5.0     | 4.5           | 0.457   | 3.4           | 1.675     |
| 18068     | 5.0     | 4.5           | 0.457   | 3.2           | 1.938     |
| 28000     | 5.1     | 4.5           | 0.544   | 2.9           | 2.452     |
| 50000     | 4.6     | 4.25          | 0.344   | 2.25          | 3.106     |

Losses are comparable to the Belden 8219 reference. The difference can most
likely be attributed to lack of precision in the measurement method or
equipment.

No doubt, 30m RG-58 is not recommended, especially not when using a 9:1
transformer with a *random wire* antenna as mismatch loss (SWR loss)
will be high.

### Combined loss

In the table below we assume 0.5 dB loss in the ATU at an SWR of 5:1
([reference][atuloss]) in addition to transmission line loss according to
previous tables in addition to the 9:1 transformer losses previously measured.
This is definitely a rough estimate.

#### ATU losses

ATU losses can be more or less depending on several circumstances, but will be
tolerable when the resistive part of the complex impedance of the antenna at
the other end of the coax is not too low at the operating frequencies of
choice. It is also important that the imaginary part is not too extreme (not
more than &#177;j200 looks like a good ballpark figure).

According to [this article][arrltnetwork], resistance need to be above 50&#937;
(&gt; 50j0) in one example on 160m to have a loss less than 0.5 dB.  In *Figure
4* in previous reference loss is 1.1 dB when R is 10&#937;, but 0.2 dB when R
is 500&#937; on 160m. *Figure 3* shows edge cases, something which will most
likely not occur with an automatic ATU, but the same thing applies here - low
resistance, high loss. Maybe the loss is insignificant, but it can be high
enough to unnecessarily make a small QRP ATU heat up.

Given that the antenna wire is long enough to be efficient on the operating
frequencies of choice, the length of the coaxial cable can have a big impact on
which resistive load the ATU sees in the other end.

For example, a *random wire* antenna I have at home has a node of very low
impedance at 17.0 MHz. It's not an amateur radio band or of any other interest
to me, so it's good that the node is there and not on, for example 18 MHz. But
let's say it was an amateur band of interest. The impedance at the end of my
coax at 17.0 MHz is 8.6+j0.87&#937;. The VSWR is slightly below 6. There will
be significant loss in the coax, which is the only thing I will have to worry
about as ATU loss at such a high frequency as 17.0 MHz will in worst case
scenario be around 0.5 dB. But let's assume we would want to improve it anyway
(maybe pretend it's 80m, where the loss would be significant in the ATU and
much less in the coax).

While playing around with [GSMC - Smith Chart Calculator][gsmc] I added 90
degrees of 50&#937; coax. 90 degrees is a quarter wave length and just happened
to transform the low resistance to something much higher. 90 degrees is 2.9
meters of extra coax, so losses will be insignificant. I could also remove 2.9m
from the coax which should have the same effect. After adding the extra coax,
the new impedance is 288-j29&#937;. According to *Figure 4* in the [ARRL
article by W4ULD][arrltnetwork], this is close to optimal loss (at least for
the 160m example). So from maximum loss to optimal loss by just adding the
right length of coax.

You may often hear that coax length *should not* matter, but in this type of
antenna it does as it acts like a transmission line transformer (VSWR is the
same though). You can find nodes of low impedance with an antenna analyzer at
the end of your coax. They say you should not measure an antenna at the end of
the coax, but at the antenna feed point. In this case, it may be less
problematic as both impedance and VSWR at the feed point can change when you
add coax in this type of antenna. It's easier to add or cut a coax you have
already installed than cutting a coax exactly according to a Smith Chart only
to find that it does not match theory.

By adding or subtracting coax (transmission line) you can move the nodes of low
impedance outside of the operating frequencies of choice (i.e outside of the
amateur radio bands). A Smith Chart is an excellent, non-computational way to
figure out which length will offset the impedance the most, but be sure to take
measurements of several bands and simulate adding the same length of coax. At
20m and above, maybe not worth it as the ATU loss is not significant on these
higher frequencies, but if you want to work 80, 40 or 30m with the 9:1
transformer, it's worth checking which impedance you have at these bands so
that both the tuner is happy and you have low loss.

If you haven't yet discovered how easy it is to transform any impedance to any
other impedance with a Smith Chart, you should learn how to use one as soon as
possible. There's a vast amount of videos on YouTube showing you how it works.

Please remember that the antenna wire need to be long enough (preferably more
than half a wave length on the lowest band of interest) or you risk
experiencing a large section with low impedance that you will have a hard time
moving, especially by adding or subtracting coax (better to extend the length
of the antenna wire).

```
$ bc
# 0.25 is another way of saying 90 degrees,
# 0.5 is 180 degrees and 1.0 is 360 degrees.
300/17.0*0.25
4.4117
# my Lappkabel RG58C/U has a velocity factor of 66%
300/17.0*0.25*0.66
2.9117
```

GSMC Smith Chart Calculator is available in most Linux distros...
```
sudo apt-get install gsmc
# another option is linsmith
sudo apt-get install linsmith
```

#### The Guesstimate

The combined loss with the 9:1 transformer (ATU + feedline + transformer) is:
> **9:1 transformer loss + feedline loss at SWR 5:1 + 0.5 dB ATU loss**

We assume a half-wave wire with the 49:1 and a perfect match (50 ohms in the
coaxial cable), thus the combined loss of the 49:1 EFHW is in this example:
> **49:1 transformer loss + feedline loss at 1:1**

#### With 10m of coax

| QRG kHz | 9:1 worst case loss (dB)  | 49:1 matched loss (dB)  |
|--------:|--------------------------:|------------------------:|
| 1800    | 3.454                     | 4.004                   |
| 3500    | 1.573                     | 2.28                    |
| 7000    | 1.384                     | 1.81                    |
| 10100   | 1.499                     | 1.744                   |
| 14000   | 1.756                     | 1.754                   |
| 18068   | 1.939                     | 1.835                   |
| 28000   | 2.340                     | 2.501                   |
| 50000   | 3.206                     | 6.923                   |

![Gnuplot 9:1 vs 49:1 system loss][svgsysloss]

[Gnuplot file of system loss][gpisysloss]

The 49:1 EFHW has more loss on all bands compared to a 9:1 *random wire* except
on 20m and 17m (and perhaps also 15m, but that was not measured). With 30m coax
the results will favour the 49:1...

#### With 30m of coax

| QRG kHz | 9:1 worst case loss (dB)  | 49:1 matched loss (dB)  |
|--------:|--------------------------:|------------------------:|
| 1800    | 4.229                     | 4.353                   |
| 3500    | 2.605                     | 2.769                   |
| 7000    | 2.757                     | 2.51                    |
| 10100   | 3.088                     | 2.591                   |
| 14000   | 3.559                     | 2.768                   |
| 18068   | 3.927                     | 2.985                   |
| 28000   | 4.682                     | 3.953                   |
| 50000   | 6.108                     | 8.91                    |

In this example the 49:1 EFHW is only worse on 160m, 80m and 6m. There is a
significant difference on 14m and 17m. However, there are significant losses in
the coax on 14m, 17m and 10m due to its length.

### Comparison with a horizontal half wave dipole

Since both the 9:1 and the 49:1 are multiband antennas (perhaps with the
exception of the 9:1 which can theoretically be used on the entire HF spectrum)
they are compromised designs. A more efficient antenna at a specific design
frequency would be a horizontal dipole. The problem is that it will most likely
only work on one band (a 40m dipole can work on 15m without an ATU).

Let's assume that we compare the 9:1 (with system losses) to a dipole on 30m.
We will need a longer coax, let's assume it's 20m compared to 10m with the 9:1.
The SWR in the coax will be 1.4 since we assume the dipole is 70 ohms. The loss
according to [CO8TW Coax Calculator][coaxcalculator] in 20m of RG-58 at 10.1
MHz is 0.887 dB which is the total loss assumed with this single band dipole.
On my YouTube channel I have references that an end-fed wire is almost
identically as efficient as a center-fed wire, so we assume the same loss in
the antenna wire. Radiation pattern can be different however.

The *random wire* system loss is 1.499 dB while the loss in the dipole is 0.887
dB (since we usually need a longer coax even when configuring it as a sloper).
The difference is 0.612 dB.

Let's take the 80m band instead, the loss in the dipole's coax is 0.515 dB,
loss in the 9:1 system is 1.573 dB, a difference of 1.1 dB. Given the fact that
the SWR will probably be lower than 5:1 with the 9:1 *random wire*, the
difference compared to a half wave dipole is not very significant. On 160m,
however, the loss is 3 dB compared to the dipole which could be said to be
significant (half an S unit). We are not comparing the same length of coax, but
you can never feed a center-fed horizontal dipole with a short coax anyway.

When comparing the dipole to a 49:1 EFHW the difference is greater, especially
in the lower end of HF, but still not highly significant (unless trying to use
it on 160m). Remember that 6 dB loss is 1 [S unit][smeter], 1.1 dB is
unnoticeable, 3 dB is half an S unit. Transmit and receive are affected equally
using any antenna (if you have loss on transmit, you have an equal amount of
loss on receive, and vice versa).

## Conclusion

With 10m coax, you can't (or you probably can) argue against the fact that the
9:1 *random wire* is more efficient despite coax and ATU losses in the lower
part of HF and 6m compared to the 49:1 EFHW. Transformer loss in the 49:1 is 1
S-unit on 6m compared to 0.6 dB loss in the 9:1 transformer. It was interesting
to find out that a 9:1 *random wire* also works well on 6m with half an S-unit
system loss. I will however not use a 49:1 on 6m. The 49:1 is better suited for
20m and 17m according to my numbers.

There may be situations where you can't use an ATU or don't want to carry
around an external ATU. Provided that you don't want to use 160m or 6m, then a
49:1 EFHW is still an excellent choice. It's well below 3 dB in loss above
160m, and 3 dB is half an S unit. An EFHW can easily be made to operate on at
least 2 major bands (3 by adding a capacitor) using the same wire (for example
40m and 20m). They are easier to mechanically tune compared to dipoles and
off-center-fed dipoles (only one end to adjust).

The 9:1 *random wire* with an ATU is not only a convenient full-spectrum HF
antenna that also works well on 6m, it's also quite efficient according to my
numbers.

The conclusion is that both systems work, and both provide good enough
efficiency to work contacts on low power. Both are below 3 dB from 80m to 10m.

I provide two Gnuplot files with this article:
[tl-transformers-9to1vs49to1.gpi][gpixfrmrloss] comparing transformer losses,
and [tl-system-9to1vs49to1.gpi][gpisysloss] comparing the estimated total
system loss.

``73 DE SA6MWA +``

[qrz]: https://www.qrz.com/db/SA6MWA
[outsender]: https://www.youtube.com/c/utesandaren
[coaxcalculator]: https://www.qsl.net/co8tw/Coax_Calculator.htm
[atuloss]: https://owenduffy.net/blog/?p=7035
[smeter]: https://en.wikipedia.org/wiki/S_meter
[arrltnetwork]: http://www.arrl.org/files/file/Technology/tis/info/pdf/9501046.pdf
[gpixfrmrloss]: tl-transformers-9to1vs49to1.gpi
[svgxfrmrloss]: tl-transformers-9to1vs49to1.svg
[gpisysloss]: tl-system-9to1vs49to1.gpi
[svgsysloss]: tl-system-9to1vs49to1.svg
[gsmc]: http://www.radioteknos.it/ik5nax_en.html
