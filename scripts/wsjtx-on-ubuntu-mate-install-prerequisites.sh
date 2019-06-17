#!/bin/bash
prerequisites=(
build-essential
gfortran
cmake
texinfo
libfftw3-dev
libhamlib-dev
qtmultimedia5-dev
libqt5multimedia5-plugins
libqt5serialport5-dev
libudev-dev
)
echo
echo "WARNING: Only for Ubuntu Mate (not tested on Ubuntu Desktop)."
echo "Will install the following packages:"
echo
for pkg in ${prerequisites[@]} ; do
  echo "  $pkg"
done
echo
echo "Press enter to continue or ctrl+c to abort..."
read input
for pkg in ${prerequisites[@]} ; do
  sudo apt-get install $pkg
done
