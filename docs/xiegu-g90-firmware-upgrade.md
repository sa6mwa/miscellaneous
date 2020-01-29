# Xiegu G90 firmware upgrade

I upgraded an early version from Linux, without 1k xmodem (just plain xmodem)
which worked fine, but recent firmware upgrades all require 1K XMODEM. The
Linux tools does support 1k xmodem, but I have not gotten that to work with the
Xiegu.

So I'm stuck using a Windows 10 virtual machine (KVM) for the upgrades.

First, connect the comm cable. In Virtual Machine Manager (under the Virtual
Machine tab), choose to *Redirect USB device*. Find the FTDI FT232R-something
device and click it, close the window. Enter Windows device manager by
executing `devmgmt` and find which COM port the FTDI device has been assigned
(Ports COM & LPT).

To transfer the firmwares to the Xiegu G90 I use ExtraPutty which can be found
on <https://www.extraputty.com>.

In ExtraPutty's Session screen (main screen) choose `Serial`. Enter the COM
port from previously and 115200 as baud rate. Hit `Open`.

Plug in the male 3.5mm TRS plug into the COMM port in the back of the G90 (main
unit) and start it. You need to be very fast by hitting `any key` before the
timeout ends. If you get `Executing user code` you have been too slow, just
turn off the G90 and try again. Once in, choose to upgrade. It will delete the
current firmware (don't worry, the boot loader and firmware upgrader is not the
same as the user code, you can't brick it).

When instructed, choose File transfer from ExtraPutty and choose 1K Xmodem.
Choose the main unit xgf file. File transfer will start.

When done you need to turn off the G90 and unplug the power cord (weird, but
necessary). Plug in the 3.5mm TRS into the display unit where there is a symbol
that looks like a person, sort of (below the headphone jack).

Start the unit again. This time you only have 2 seconds to press any key to
enter the firmware upgrade menu. Just repeat if you fail. Do the same thing,
file transfer, 1k xmodem, choose the main unit xgf firmware file. When done the
G90 will load the `user code` and the transceiver will start with the new
firmware. I usually power it off and unplug, then replug the power cord, just
in case.

