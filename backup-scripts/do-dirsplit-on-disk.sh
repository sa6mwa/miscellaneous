#!/bin/bash -xe
#
## To be used with dirsplit, for example:
#
# dirsplit -s 4G -v -e1 dirtosplit/
#
## will produce vol_?.list files for use with this script
##
## Usage:
#
# do-dirsplit-on-disk.sh vol_1.list outputdir01
#
## If you want to move and not copy the files, change the "move" command to mv:
# do-dirsplit-on-disk.sh vol_1.list outputdir01 mv

volfile=${1:-vol_1.list}
outdir=${2:-vol_1}
mvcmd=${3:-cp}

if [ ! -f "${volfile}" ]; then
  echo "usage: splitem.sh vol_1.list [outputdir01] [mv]"
  exit 1
fi

cat $volfile | cut -d= -f2 | while read -r f
do
if [ -f "$f" ]; then
  p="${f#${PWD}/}"
  d=$(dirname "$p")
  mkdir -p "$outdir/$d"
  "$mvcmd" -i "$f" "$outdir/$p"
fi
done
