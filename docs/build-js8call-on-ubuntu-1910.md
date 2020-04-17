# Build js8call on Ubuntu 19.10 (eoan)

Instructions from <https://9a3gos.com/install-js8call-2-0-0-rc3-on-ubuntu-19-10-hamlib/> ...

```shell
sudo apt-get install -y build-essential gfortran autoconf automake libtool cmake git asciidoctor libfftw3-dev qtdeclarative5-dev texinfo libqt5multimedia5 libqt5multimedia5-plugins qtmultimedia5-dev libusb-1.0.0-dev libqt5serialport5-dev asciidoc libudev-dev

mkdir -p ~/src/hamlib
cd ~/src/hamlib
git clone git://git.code.sf.net/u/bsomervi/hamlib src
cd src
git checkout integration
./bootstrap
mkdir ../build
cd ../build
../src/configure --prefix=$HOME/hamlib --disable-shared --enable-static --without-cxx-binding --disable-winradio CFLAGS="-g -O2 -fdata-sections -ffunction-sections" LDFLAGS="-Wl,--gc-sections"
make -j4
make install-strip

VER=2.1.1
cd ~/src
wget http://files.js8call.com/$VER/js8call-$VER.tgz
tar -xf js8call-$VER.tgz
cd js8call-$VER
cmake -D hamlib_LIBRARY_DIRS=~/hamlib -D CMAKE_INSTALL_PREFIX=~/src/js8call-$VER/output
cmake --build . -- -j4
#
## if you get the following error...
#
#~/src/js8call-2.1.1/HamlibTransceiver.hpp:20:24: error: conflicting declaration ‘typedef unsigned int vfo_t’
#   20 |   typedef unsigned int vfo_t;
#      |                        ^~~~~
#In file included from ~/src/js8call-2.1.1/HamlibTransceiver.hpp:8,
#                 from ~/src/js8call-2.1.1/HamlibTransceiver.cpp:1:
#/usr/include/hamlib/rig.h:350:13: note: previous declaration as ‘typedef int vfo_t’
#  350 | typedef int vfo_t;
#
## remove the entire extern "C" block from HamlibTransceiver.hpp (where typedef unsigned int vfo_t is defined)

# make symlink
sudo ln -s ~/src/js8call-$VER/js8call /usr/local/bin/js8call 
```
