#!/bin/bash
#
# Audible aax file activation_bytes resolver via ffprobe and rcrack.
# Helper for rcrack https://github.com/inAudible-NG/tables
#
# Clone the tables repo and put this file in the top directory,
# run with first argument pointing to your downloaded aax.
# If successful, ffprobe will retrieve the checksum and rcrack
# will brute-force the activation_bytes.
#
# With the activation_bytes, you can play and recode the aax into another
# format via fmpeg.
#
# ffmpeg -activation_bytes=123456 -i my.aax output.wav

set -euo pipefail

if [ $# -lt 1 ]; then
	echo "usage: $0 in.aax"
	echo "requires ffprobe on the path"
	exit 1
fi

chksum=$(ffprobe $1 2>&1 | grep -o 'checksum == .*' | cut -d' ' -f3)

./rcrack . -h ${chksum}
