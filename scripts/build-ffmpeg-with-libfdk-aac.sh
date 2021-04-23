#!/bin/bash
if [ "$1" != "okilidokili" ]; then
  echo "This script is tailored for Ubuntu Mate 20.10 groovy and"
  echo "may not build on other debian-based systems."
  echo "Also confirmed working for: Ubuntu 20.04.2 LTS focal"
  echo "Good to go? Build like this..."
  echo
  echo "$0 okilidokili"
  exit
fi

set -xe

if [ ! -d ffmpeg_source ]; then
  mkdir ffmpeg_source
  cd ffmpeg_source
fi

sudo apt-get update -qq
sudo apt-get install \
  autoconf \
  automake \
  build-essential \
  cmake \
  git-core \
  libass-dev \
  libfreetype6-dev \
  libunistring-dev \
  libgnutls28-dev \
  libsdl2-dev \
  libtool \
  libva-dev \
  libvdpau-dev \
  libvorbis-dev \
  libxcb1-dev \
  libxcb-shm0-dev \
  libxcb-xfixes0-dev \
  pkg-config \
  texinfo \
  wget \
  yasm \
  zlib1g-dev \
  nasm \
  libx264-dev \
  libx265-dev \
  libnuma-dev \
  libvpx-dev \
  libfdk-aac-dev \
  libmp3lame-dev \
  libopus-dev \
  libchromaprint-dev \
  frei0r-plugins-dev \
  ladspa-sdk \
  libcaca-dev \
  libcdio-paranoia-dev \
  libcodec2-dev \
  libfontconfig1-dev \
  libfribidi-dev \
  libgme-dev \
  libgsm1-dev \
  libjack-dev \
  libmodplug-dev \
  libopencore-amrnb-dev \
  libopencore-amrwb-dev \
  libopenjp2-7-dev \
  libopenmpt-dev \
  libpulse-dev \
  librsvg2-dev \
  librubberband-dev \
  librtmp-dev \
  libshine-dev \
  libsmbclient-dev \
  libsnappy-dev \
  libsoxr-dev \
  libspeex-dev \
  libssh-dev \
  libtesseract-dev \
  libtheora-dev \
  libtwolame-dev \
  libv4l-dev \
  libvo-amrwbenc-dev \
  libwavpack-dev \
  libwebp-dev \
  libxvidcore-dev \
  libxml2-dev \
  libzmq3-dev \
  libzvbi-dev \
  liblilv-dev \
  libopenal-dev \
  opencl-dev \
  libavc1394-0 \
  libavc1394-dev \
  libiec61883-0 \
  libiec61883-dev \
  libbluray-dev \
  libbs2b-dev \
  libbs2b0 \
  libdc1394-25 \
  libdc1394-dev \
  libdrm-dev

git -C aom pull 2> /dev/null || git clone --depth 1 https://aomedia.googlesource.com/aom
mkdir -p aom_build
pushd aom_build
PATH="$HOME/bin:$PATH" cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="$HOME/ffmpeg" -DBUILD_SHARED_LIBS=1 -DENABLE_NASM=on ../aom
PATH="$HOME/bin:$PATH" make
make install
popd

wget -O ffmpeg-snapshot.tar.bz2 https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
tar xjvf ffmpeg-snapshot.tar.bz2
pushd ffmpeg
PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg/lib/pkgconfig" ./configure \
  --disable-static \
  --enable-shared \
  --disable-stripping \
  --prefix="$HOME/ffmpeg" \
  --extra-cflags="-I$HOME/ffmpeg/include" \
  --extra-ldflags="-L$HOME/ffmpeg/lib" \
  --bindir="$HOME/bin" \
  --enable-gpl \
  --enable-gnutls \
  --enable-libaom \
  --enable-libass \
  --enable-libfdk-aac \
  --enable-libfreetype \
  --enable-libmp3lame \
  --enable-libopus \
  --enable-libvorbis \
  --enable-libvpx \
  --enable-libx264 \
  --enable-libx265 \
  --enable-avresample \
  --enable-chromaprint \
  --enable-frei0r \
  --enable-gmp \
  --enable-ladspa \
  --enable-libbluray \
  --enable-libbs2b \
  --enable-libcaca \
  --enable-libcdio \
  --enable-libcodec2 \
  --enable-libdc1394 \
  --enable-libdrm \
  --enable-libfontconfig \
  --enable-libfribidi \
  --enable-libgme \
  --enable-libgsm \
  --enable-libiec61883 \
  --enable-libjack \
  --enable-libmodplug \
  --enable-libopencore-amrnb \
  --enable-libopencore-amrwb \
  --enable-libopenjpeg \
  --enable-libopenmpt \
  --enable-libpulse \
  --enable-librsvg \
  --enable-librtmp \
  --enable-librubberband \
  --enable-libshine \
  --enable-libsnappy \
  --enable-libsoxr \
  --enable-libspeex \
  --enable-libssh \
  --enable-libtesseract \
  --enable-libtheora \
  --enable-libtwolame \
  --enable-libv4l2 \
  --enable-libvo-amrwbenc \
  --enable-libvpx \
  --enable-libwebp \
  --enable-libxml2 \
  --enable-libxvid \
  --enable-libzmq \
  --enable-libzvbi \
  --enable-lv2 \
  --enable-openal \
  --enable-opencl \
  --enable-opengl \
  --enable-sdl2 \
  --enable-version3 \
  --enable-nonfree \
  --enable-small

PATH="$HOME/bin:$PATH" make
make install
popd

cat <<EOF

# You need to add the following to your .bashrc or similar:
export LD_LIBRARY_PATH="\$LD_LIBRARY_PATH:\$HOME/ffmpeg/lib"

# If you do not have \$HOME/bin in your path (echo \$PATH),
# add it to .bashrc also...
export PATH="\$HOME/bin:\$PATH"

EOF
